from argparse import ArgumentParser
import string, random

# include payload generators
from generators.xgen import XssGen
from generators.php import PHPCodeInjectionGenerator
from generators.ored import OpenRedirectionPayloadGenerator
from generators.ssti import TemplateInjectionGenerator
from generators.sqli import SQLIGenerator
from generators.ssi import SSIPayloadGenerator
from generators.traversal import DirectoryTraversalPayloadGenerator
from generators.htmli import HTMLInjectionPayloadGenerator


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


    # ---------------------------------- [ Open Redirection Parsing ] -----------------------------------------
    
    ored_parser = subparsers.add_parser("ored", help="Generate Open Redirection Payloads")


    ored_options = ored_parser.add_argument_group("Open Redirection Payload Options")
    ored_options.add_argument("--oast-domain", dest="oast_domain", metavar="", help="Set OAST Domain for payloads")
    ored_options.add_argument("--unique-string", dest="unique_string", metavar="", help="Set Unique String for testing")
    ored_options.add_argument("--whitelisted-domain", dest="whitelisted_domain", metavar="", help="Set Whitelisted domain for testing")
    ored_options.add_argument("--xss-payloads", dest="xss_payloads", action="store_true", help="Generate XSS Payloads")
    
    ored_mutator = ored_parser.add_argument_group("Open Redirection Payload Mutations")
    ored_mutator.add_argument("--urlencode",dest="urlencode", action="store_true", help="Set URL Encoding for payload generator")


     # ---------------------------------- [ Servier-Side Template Injection Parsing ] -----------------------------------------
    
    ssti_parser = subparsers.add_parser("ssti", help="Service-Side Template Injection Payloads")
    
    ssti_payload_selector = ssti_parser.add_argument_group("Service-Side Template Injection Payload Types") 
    ssti_payload_selector.add_argument("--reflective", dest="reflective_payloads", action="store_true", help="Generate reflective payloads")
    ssti_payload_selector.add_argument("--oast", dest="oast_payloads", action="store_true", help="Generate OAST payloads")
    ssti_payload_selector.add_argument("--timeout", dest="timeout_payloads", action="store_true", help="Generate Time-Based payloads")

    ssti_options = ssti_parser.add_argument_group("Service-Side Template Injection Payload Options")
    ssti_options.add_argument("--oast-domain", dest="oast_domain", metavar="", help="Set OAST Domain for payloads")
    ssti_options.add_argument("--unique-string", dest="unique_string", metavar="", help="Set Unique String for testing")
    ssti_options.add_argument("--sleep-timeout", dest="sleep_timeout", type=int, metavar="", help="Set Sleep Timeout for payload genrating")
    ssti_options.add_argument("--number", dest="number", metavar="", type=int, help="Set number for payload genrating")
    ssti_options.add_argument("--multiply", dest="multiply", metavar="", type=int, help="Set string multiply number for payload genrating")

    ssti_platform_selector = ssti_parser.add_argument_group("SSTI Platform Options")
    ssti_platform_selector.add_argument("-w","--windows", dest="windows_platform", action="store_true", help="Generate Windows Based payloads")
    ssti_platform_selector.add_argument("-l","--linux", dest="linux_platform", action="store_true", help="Generate Linux Based payloads")
    
    
    ssti_mutator = ssti_parser.add_argument_group("Server Side Template Injection Payload Mutations")
    ssti_mutator.add_argument("--urlencode",dest="urlencode", action="store_true", help="Set URL Encoding for payload generator")

    # ---------------------------------- [ SQL Injection Parsing ] -----------------------------------------
    
    sqli_parser = subparsers.add_parser("sqli", help="SQL Injection Payloads")
    
    sqli_payload_selector = sqli_parser.add_argument_group("SQL Injection Payload Types") 
    sqli_payload_selector.add_argument("--error-based", dest="error_based", action="store_true", help="Generate Error Based payloads")
    sqli_payload_selector.add_argument("--time-based", dest="time_based", action="store_true", help="Generate Time Based payloads")
    sqli_payload_selector.add_argument("--union-based", dest="union_based", action="store_true", help="Generate Union Based payloads")
    sqli_payload_selector.add_argument("--auth-bypass", dest="auth_bypass", action="store_true", help="Generate Auth Bypass payloads")

    sqli_options = sqli_parser.add_argument_group("SQL Injection Payload Options")
    sqli_options.add_argument("--sleep-timeout", dest="sleep_timeout", type=int, metavar="", help="Set Sleep Timeout for payload genrating")

    # ---------------------------------- [ SSI Parsing ] -----------------------------------------
    
    ssi_parser = subparsers.add_parser("ssi", help="SSI Payloads")
    
    ssi_payload_selector = ssi_parser.add_argument_group("SSI Payload Types") 
    ssi_payload_selector.add_argument("--reflective", dest="reflective_payloads", action="store_true", help="Generate Reflective payloads")
    ssi_payload_selector.add_argument("--time-based", dest="timeout_payloads", action="store_true", help="Generate Time Based payloads")
    ssi_payload_selector.add_argument("--oast", dest="oast_payloads", action="store_true", help="Generate OAST payloads")

    ssi_options = ssi_parser.add_argument_group("SSI Payload Options")
    ssi_options.add_argument("--sleep-timeout", dest="sleep_timeout", type=int, metavar="", help="Set Sleep Timeout for payload genrating")
    ssi_options.add_argument("--oast-domain", dest="oast_domain",  metavar="", help="Set OAST Domain for payload genrating")
    ssi_options.add_argument("--unique-string", dest="unique_string", metavar="", help="Set Unique string for payload genrating")
    
    ssi_platform_selector = ssi_parser.add_argument_group("SSI Platform Options")
    ssi_platform_selector.add_argument("-w","--windows", dest="windows_platform", action="store_true", help="Generate Windows Based payloads")
    ssi_platform_selector.add_argument("-l","--linux", dest="linux_platform", action="store_true", help="Generate Linux Based payloads")
    
    
    ssi_mutator = ssi_parser.add_argument_group("SSI Payload Mutations")
    ssi_mutator.add_argument("--urlencode",dest="urlencode", action="store_true", help="Set URL Encoding for payload generator")


     # ---------------------------------- [ Directory Traversal Parsing ] -----------------------------------------
    
    dt_parser = subparsers.add_parser("traversal", help="File & Path Traversal Payloads")
    dt_payload_selector = dt_parser.add_argument_group("File & Path Traversal Payload Types")
    dt_payload_selector.add_argument("--file-traversal", dest="file_traversal", action="store_true", help="Generate File Traversal Payloads")
    dt_payload_selector.add_argument("--path-traversal", dest="path_traversal", action="store_true", help="Generate Path Traversal Payloads")
    dt_payload_selector.add_argument("--all", dest="all_traversal", action="store_true", help="Generate All Traversal Payloads")


    dt_payload_options = dt_parser.add_argument_group("File & Path Traversal Payload Options")
    dt_payload_options.add_argument("--depth", dest="traversal_depth", metavar="", type=int, default=8, help="Generated Traversal Depth")
    dt_payload_options.add_argument("--custom-file", dest="custom_file", metavar="", nargs="+", action="extend", help="Generated Traversal Depth")
    dt_payload_options.add_argument("--custom-path", dest="custom_path", metavar="", nargs="+", action="extend", help="Generated Traversal Depth")

    dt_platform_selector = dt_parser.add_argument_group("File & Path Traversal Platform Options")
    dt_platform_selector.add_argument("-w","--windows", dest="windows_platform", action="store_true", help="Generate Windows Based payloads")
    dt_platform_selector.add_argument("-l","--linux", dest="linux_platform", action="store_true", help="Generate Linux Based payloads")
    
    dt_mutator = dt_parser.add_argument_group("File & Path Traversal Payload Mutations")
    dt_mutator.add_argument("--urlencode", dest="urlencode", action="store_true", help="Set URL Encoding for Payloads")

    # ---------------------------------- [ HTML Injection Parsing ] -----------------------------------------
    
    htmli_parser = subparsers.add_parser("htmli", help="HTML Injection Payloads")
    htmli_payload_selector = htmli_parser.add_argument_group("HTML Injection Payload Types")    
    htmli_payload_selector.add_argument("--html-tags", dest="html_tags", action="store_true", help="Generate HTML tags")
    htmli_payload_selector.add_argument("--html-events", dest="html_events", action="store_true", help="Generate HTML Events")
    htmli_payload_selector.add_argument("--combo-list", dest="combo_list", action="store_true", help="Generate Combo List")


    htmli_options = htmli_parser.add_argument_group("HTML Injection Payload Options")
    #htmli_options.add_argument("--oast-domain", dest="oast_domain",  metavar="", help="Set OAST Domain for payload genrating")
    htmli_options.add_argument("--unique-string", dest="unique_string", metavar="", help="Set Unique string for payload genrating")
    htmli_options.add_argument("--tag", dest="html_tag", metavar="", nargs="+", action="extend", help="Set Unique TAG for payload genrating")
    htmli_options.add_argument("--event", dest="html_event", metavar="", nargs="+", action="extend", help="Set Unique TAG for payload genrating")
    htmli_options.add_argument("--include-id", dest="include_id", action="store_true", help="Include ID into payloads")
    htmli_options.add_argument("--payload", dest="payloads", metavar="", nargs="+", action="extend", help="Add Custom Payloads")
    


    htmli_mutator = htmli_parser.add_argument_group("HTML Injection Payload Mutations")
    htmli_mutator.add_argument("--urlencode", dest="urlencode", action="store_true", help="Set URL Encoding for Payloads")
    htmli_mutator.add_argument("--strip-space", dest="stripspace", action="store_true", help="Change space in Payloads")
    htmli_mutator.add_argument("--tag-breaking", dest="tag_breaking", action="store_true", help="Apply Tag Breaking")
    htmli_mutator.add_argument("--null-byte", dest="null_byte", action="store_true", help="Apply Null Byte Injection")


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
        php.sleep_timeout = sleep_timeout


        result_payloads.extend(php.generate_payloads())

    if args.payload_type == 'ored':
        if args.oast_domain: oast_domain = args.oast_domain
        if args.unique_string: unique_string = args.unique_string

        
        ored = OpenRedirectionPayloadGenerator()
        ored.unique_string = unique_string
        ored.url_encode = args.urlencode if args.urlencode else False 
        ored.domain = oast_domain
        if args.whitelisted_domain: ored.whitelisted = args.whitelisted_domain 
        
        if args.xss_payloads:
            result_payloads.extend(ored.generate_xss_payloads())
        else:
            result_payloads.extend(ored.generate_payloads())

    if args.payload_type == 'ssti':
        if args.oast_domain: oast_domain = args.oast_domain
        if args.unique_string: unique_string = args.unique_string
        if args.sleep_timeout: sleep_timeout = args.sleep_timeout
        
        ssti = TemplateInjectionGenerator()
        ssti.unique_string = unique_string
        #ssti.url_encode = args.urlencode if args.urlencode else False 
        ssti.domain = oast_domain
        ssti.sleep_timeout = sleep_timeout
        if args.number: ssti.number = args.number
        if args.multiply: ssti.multiply_string = args.multiply
        if args.urlencode: ssti.url_encode_payloads = True 
        
        if args.windows_platform and args.linux_platform or not args.linux_platform and not args.windows_platform:
            ssti.platforms = ['linux', 'windows']
        
        if args.windows_platform and not args.linux_platform:
            ssti.platforms = ["windows"]
        
        if not args.windows_platform and args.linux_platform:
            ssti.platforms = ["linux"]

        if args.reflective_payloads:
            result_payloads.extend(ssti.generate_reflective_payloads())
        
        if args.timeout_payloads:
            result_payloads.extend(ssti.generate_time_based_payloads())

        if args.oast_payloads:
            result_payloads.extend(ssti.generate_oast_payloads())

    if args.payload_type == 'sqli':
        if args.sleep_timeout: sleep_timeout = args.sleep_timeout
        
        sqli = SQLIGenerator()
        sqli.sleep_timeout = sleep_timeout
        
        if args.error_based:
            result_payloads.extend(sqli.generate_error_based_payloads())
        if args.time_based:
            result_payloads.extend(sqli.generate_time_based_payloads())
        if args.union_based:
            result_payloads.extend(sqli.generate_union_select_payloads())
        if args.auth_bypass:
            result_payloads.extend(sqli.generate_auth_bypass())

    if args.payload_type == 'ssi':
        if args.oast_domain: oast_domain = args.oast_domain
        if args.unique_string: unique_string = args.unique_string
        if args.sleep_timeout: sleep_timeout = args.sleep_timeout
        
        ssi = SSIPayloadGenerator()
        ssi.unique_string = unique_string
        ssi.domain = oast_domain
        ssi.sleep_timeout = sleep_timeout
        if args.urlencode: ssi.url_encode_payloads = True 
        
        if args.windows_platform and args.linux_platform or not args.linux_platform and not args.windows_platform:
            ssi.platforms = ['linux', 'windows']
        
        if args.windows_platform and not args.linux_platform:
            ssi.platforms = ["windows"]
        
        if not args.windows_platform and args.linux_platform:
            ssi.platforms = ["linux"]

        if args.reflective_payloads:
            result_payloads.extend(ssi.generate_reflective_payloads())
        
        if args.timeout_payloads:
            result_payloads.extend(ssi.generate_time_based_payloads())

        if args.oast_payloads:
            result_payloads.extend(ssi.generate_oast_payloads())

    if args.payload_type == 'traversal':
        
        dt = DirectoryTraversalPayloadGenerator()
        if args.traversal_depth: dt.depth = args.traversal_depth
        if args.urlencode: dt.url_encode_payload = True 
        
        
        if args.windows_platform and args.linux_platform or not args.linux_platform and not args.windows_platform:
            dt.platforms = ['linux', 'windows']
        
        if args.windows_platform and not args.linux_platform:
            dt.platforms = ["windows"]
        
        if not args.windows_platform and args.linux_platform:
            dt.platforms = ["linux"]

        # Custom file processation placed here to override platform settings at above

        if args.custom_file:
            dt.os_files.extend([('custom',f) for f in args.custom_file])
            dt.platforms = ["custom"]
        if args.custom_path:
            dt.os_paths.extend([('custom',f) for f in args.custom_path])
            dt.platforms = ["custom"]

        # Generate payloads
        if args.file_traversal:
            result_payloads.extend(dt.generate_file_payloads())
        if args.path_traversal:
            result_payloads.extend(dt.generate_path_payloads())
        if args.all_traversal:
            result_payloads.extend(dt.generate_all_payloads())

    if args.payload_type == 'htmli':
        
        htmli = HTMLInjectionPayloadGenerator()
        htmli.unique_string = unique_string
        htmli.domain = oast_domain
        if args.urlencode: htmli.url_encode_payloads = True 
        #if args.oast_domain: htmli.domain = args.oast_domain
        if args.unique_string: htmli.unique_string = args.unique_string
        if args.stripspace: htmli.change_spaces = True
        if args.include_id: htmli.include_id = True
        if args.tag_breaking: htmli.tag_break = True
        if args.null_byte: htmli.null_byte = True

        if args.html_tag:
            htmli.html_tags = args.html_tag
        if args.html_event:
            htmli.html_events = args.html_event
        if args.payloads:
            htmli.custom_payloads = args.payloads 



        if args.html_tags:
            result_payloads.extend(htmli.get_html_tags())
        if args.html_events:
            result_payloads.extend(htmli.get_html_attributes())
        if args.combo_list:
            result_payloads.extend(htmli.generate_all_tags_all_attributes())


    for payload in result_payloads:
        print(payload)


if __name__ == '__main__':
    main()