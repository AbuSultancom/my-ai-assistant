#!/usr/bin/env python3
"""
Abu Remote - التحكم عن بُعد
==========================
يسمح لـ أبو بالتحكم بـ TITAN من OpenClaw
"""

import sys
import json
from pathlib import Path

# إضافة مسار TITAN
sys.path.insert(0, str(Path.home() / 'TITAN'))
sys.path.insert(0, '/home/abdulhameed/TITAN')

try:
    from titan_bridge import send_to_titan, get_from_titan, get_bridge
except ImportError as e:
    print(f"❌ خطأ في استيراد TITAN Bridge: {e}")
    sys.exit(1)


def send_command(command: str, wait_for_response: bool = True, timeout: int = 30):
    """
    إرسال أمر إلى TITAN وانتظار الرد
    
    الاستخدام:
        python3 abu_remote.py "افتح Chrome"
        python3 abu_remote.py "صورة للشاشة"
        python3 abu_remote.py "شغل الأمر: ls -la"
    """
    print(f"📝 إرسال الأمر: {command}")
    
    # إرسال الأمر
    cmd_id = send_to_titan(command)
    print(f"📤 معرف الأمر: {cmd_id}")
    
    if not wait_for_response:
        return {'status': 'sent', 'id': cmd_id}
    
    # انتظار الرد
    print("⏳ انتظار الرد...")
    import time
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        responses = get_from_titan()
        
        for resp in responses:
            if resp.get('id') == cmd_id:
                result = resp.get('result', {})
                
                if result.get('success'):
                    print(f"✅ نجح الأمر!")
                    print(f"📄 النتيجة:\n{result.get('output', 'لا يوجد')}")
                else:
                    print(f"❌ فشل الأمر")
                    print(f"⚠️ الخطأ: {result.get('error', 'خطأ غير معروف')}")
                
                return result
        
        time.sleep(0.5)
    
    print("⏰ انتهى الوقت في انتظار الرد")
    return {'status': 'timeout', 'id': cmd_id}


def get_status():
    """الحصول على حالة TITAN"""
    bridge = get_bridge()
    status = bridge.get_status()
    
    print("📊 حالة TITAN:")
    print(json.dumps(status, indent=2))
    
    return status


def list_pending_commands():
    """عرض الأوامر المعلقة"""
    bridge = get_bridge()
    commands = bridge.check_for_commands()
    
    if not commands:
        print("📭 لا يوجد أوامر معلقة")
        return []
    
    print(f"📬 {len(commands)} أوامر معلقة:")
    for cmd in commands:
        print(f"  - [{cmd.id}] {cmd.command}")
    
    return commands


def clear_all():
    """مسح جميع الأوامر والردود"""
    bridge = get_bridge()
    bridge.clear_inbox()
    bridge.clear_outbox()
    print("🧹 تم مسح جميع الأوامر والردود")


def main():
    """الدالة الرئيسية"""
    import argparse
    
    parser = argparse.ArgumentParser(description='أبو - التحكم في TITAN')
    parser.add_argument('command', nargs='?', help='الأمر المراد تنفيذه')
    parser.add_argument('--status', action='store_true', help='عرض الحالة')
    parser.add_argument('--pending', action='store_true', help='عرض الأوامر المعلقة')
    parser.add_argument('--clear', action='store_true', help='مسح جميع الأوامر')
    parser.add_argument('--no-wait', action='store_true', help='لا تنتظر الرد')
    parser.add_argument('--timeout', type=int, default=30, help='مهلة الانتظار (ثواني)')
    
    args = parser.parse_args()
    
    if args.status:
        get_status()
    
    elif args.pending:
        list_pending_commands()
    
    elif args.clear:
        clear_all()
    
    elif args.command:
        send_command(
            args.command,
            wait_for_response=not args.no_wait,
            timeout=args.timeout
        )
    
    else:
        # وضع تفاعلي
        print("🤖 أبو - وضع التحكم في TITAN")
        print("اكتب 'exit' للخروج\n")
        
        while True:
            try:
                cmd = input("📝 أمر: ").strip()
                
                if not cmd:
                    continue
                
                if cmd.lower() in ['exit', 'quit']:
                    print("👋 مع السلامة!")
                    break
                
                if cmd == 'status':
                    get_status()
                elif cmd == 'pending':
                    list_pending_commands()
                elif cmd == 'clear':
                    clear_all()
                else:
                    send_command(cmd)
                
            except KeyboardInterrupt:
                print("\n👋 مع السلامة!")
                break
            except Exception as e:
                print(f"❌ خطأ: {e}")


if __name__ == '__main__':
    main()
