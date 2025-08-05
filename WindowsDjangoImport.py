Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Users\eoneill> pip install Django
pip : The term 'pip' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ pip install Django
+ ~~~
    + CategoryInfo          : ObjectNotFound: (pip:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\eoneill> py -m pip install Django
Defaulting to user installation because normal site-packages is not writeable
Collecting Django
  Downloading django-5.2.4-py3-none-any.whl.metadata (4.1 kB)
Collecting asgiref>=3.8.1 (from Django)
  Downloading asgiref-3.9.1-py3-none-any.whl.metadata (9.3 kB)
Collecting sqlparse>=0.3.1 (from Django)
  Downloading sqlparse-0.5.3-py3-none-any.whl.metadata (3.9 kB)
Collecting tzdata (from Django)
  Downloading tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
Downloading django-5.2.4-py3-none-any.whl (8.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.3/8.3 MB 28.9 MB/s  0:00:00
Downloading asgiref-3.9.1-py3-none-any.whl (23 kB)
Downloading sqlparse-0.5.3-py3-none-any.whl (44 kB)
Downloading tzdata-2025.2-py2.py3-none-any.whl (347 kB)
Installing collected packages: tzdata, sqlparse, asgiref, Django
   ━━━━━━━━━━╺━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1/4 [sqlparse]  WARNING: The script sqlformat.exe is installed in 'C:\Users\eoneill\AppData\Roaming\Python\Python313\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╺━━━━━━━━━ 3/4 [Django]  WARNING: The script django-admin.exe is installed in 'C:\Users\eoneill\AppData\Roaming\Python\Python313\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed Django-5.2.4 asgiref-3.9.1 sqlparse-0.5.3 tzdata-2025.2
PS C:\Users\eoneill> django-admin start
                     django-admin startproject TrialChecker
django-admin : The term 'django-admin' is not recognized as the name of a cmdlet, function, script file, or operable
program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ django-admin startproject TrialChecker
+ ~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (django-admin:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\eoneill> django-admin startproject TrialChecker
django-admin : The term 'django-admin' is not recognized as the name of a cmdlet, function, script file, or operable
program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ django-admin startproject TrialChecker
+ ~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (django-admin:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\eoneill> django-admin startproject TrialChecker
django-admin : The term 'django-admin' is not recognized as the name of a cmdlet, function, script file, or operable
program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ django-admin startproject TrialChecker
+ ~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (django-admin:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\eoneill> & "C:\Users\eoneill\AppData\Roaming\Python\Python313\Scripts\django-admin.exe" startproject TrialChecker
PS C:\Users\eoneill> where django-admin
PS C:\Users\eoneill>
