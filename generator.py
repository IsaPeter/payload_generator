from argparse import ArgumentParser
import string, random

# include payload generators
from generators.xgen import XssGen
from generators.php import PHPCodeInjectionGenerator


def parse_arguments():
    parser = ArgumentParser(description="Payload Generator")

    subparsers = parser.add_subparsers(dest="payload_type", help="Select Option")
    
    # ---------------------------------- [ XSS Parsing ] -----------------------------------------
    xss_parser = subparsers.add_parser("xss", help="Generate XSS Payloads")
    xss_payload_selector = xss_parser.add_argument_group("XSS Payload Types")
    xss_payload_selector.add_argument("--popup", dest="popup_payloads", action="store_true", help="Generate Popup Payloads")
    xss_payload_selector.add_argument("--logger", dest="logger_payloads", action="store_true", help="Generate Console.log() Payloads")
    xss_payload_selector.add_argument("--oast", dest="oast_payloads", action="store_true", help="Generate OAST Payloads")
    xss_payload_selector.add_argument("--dom", dest="dom_payloads", action="store_true", help="Generate DOM Payloads")
    xss_payload_selector.add_argument("--ored", dest="ored_payloads", action="store_true", help="Generate ORED Payloads")

    xss_options = xss_parser.add_argument_group("XSS Payload Options")
    xss_options.add_argument("--oast-domain",dest="oast_domain", metavar="", help="Set OAST Domain for payloads")
    xss_options.add_argument("--unique-string",dest="unique_string", metavar="", help="Set Unique String for testing")
    

    xss_mutator = xss_parser.add_argument_group("XSS Payload Mutations")
    xss_mutator.add_argument("--waf", dest="waf_bypass", action="store_true", help="Generate WAF Bypass Payloads")
    xss_mutator.add_argument("--reverse-payloads", dest="reverse_payloads", action="store_true", help="Generate Reverse Payloads")
    xss_mutator.add_argument("--urlencode",dest="urlencode", action="store_true", help="Set URL Encoding for payload generator")
    
    # ---------------------------------- [ PHP Code Injection Parsing ] -----------------------------------------
    
    php_parser = subparsers.add_parser("php", help="Generate PHP Code Injection Payloads")
    php_options = php_parser.add_argument_group("PHP CI Payload Options")
    php_options.add_argument("--oast-domain", dest="oast_domain", metavar="", help="Set OAST Domain for payloads")
    php_options.add_argument("--unique-string", dest="unique_string", metavar="", help="Set Unique String for testing")
    php_options.add_argument("--sleep-timeout", dest="sleep_timeout", metavar="" , type=int, help="Set Sleep Timeout")

    php_mutator = php_parser.add_argument_group("PHP Payload Mutations")
    php_mutator.add_argument("--urlencode",dest="urlencode", action="store_true", help="Set URL Encoding for payload generator")

    return parser.parse_args()

def main():
    args = parse_arguments()
    sleep_timeout = 15
    oast_domain = "127.0.0.1"
    unique_string = ''.join(random.choice(string.ascii_uppercase+ string.ascii_lowercase + string.digits) for _ in range(20)) # Generate unique string

    result_payloads = []
    


    if args.payload_type == 'xss':
        if args.oast_domain: oast_domain = args.oast_domain
        if args.unique_string: unique_string = args.unique_string
        
        waf_bypass = args.waf_bypass if args.waf_bypass else False
        reverse_payloads = args.reverse_payloads if args.reverse_payloads else False
        
        xss = XssGen()
        xss.waf_bypass = waf_bypass
        xss.reverse_payload = reverse_payloads
        xss.unique_string = unique_string
        xss.url_encode = args.urlencode if args.urlencode else False 
        xss.domain = oast_domain



        if args.popup_payloads:
            result_payloads.extend(xss.generate_popup_payloads())

        if args.logger_payloads:
            result_payloads.extend(xss.generate_logger_payloads())

        if args.oast_payloads:
            result_payloads.extend(xss.generate_oast_payloads())

        if args.dom_payloads:
            result_payloads.extend(xss.generate_dom_modify_payloads())

        if args.ored_payloads:
            result_payloads.extend(xss.generate_ored_payloads())

    if args.payload_type == 'php':
        if args.oast_domain: oast_domain = args.oast_domain
        if args.unique_string: unique_string = args.unique_string
        if args.sleep_timeout: sleep_timeout = args.sleep_timeout
        
        php = PHPCodeInjectionGenerator()
        php.unique_string = unique_string
        php.url_encode_payloads = args.urlencode if args.urlencode else False 
        php.domain = oast_domain


        result_payloads.extend(php.generate_payloads())



    for payload in result_payloads:
        print(payload)


if __name__ == '__main__':
    main()