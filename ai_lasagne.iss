; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "AI Lasagne Generator 3000"
; Change the version number below in case you want to update your installer
#define MyAppVersion "1.3"
; Add you Publisher name here
#define MyAppPublisher "Your Name Here"
; Add your URL here
#define MyAppURL "http://www.example.com/"
#define MyAppExeName "AI Lasagne Generator.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
; Generate a new GUID using the Tools menu
AppId={{AAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
; Add a License file
LicenseFile=Path to License file
; Add a Readme file
InfoBeforeFile=Path to Readme file
; Add a Thanks file
InfoAfterFile=Path to Thanks file
; Remove the following line to run in administrative install mode (install for all users.)
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=commandline
; Add your output directory here
OutputDir=Add your output directory here
OutputBaseFilename=AI_Lasagne_Generator_3K
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
; You can add more languages if you want
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "french"; MessagesFile: "compiler:Languages\French.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
; Here is all the files that will be installed change all the paths to match your files (Here is an example)
Source: "C:\Users\User\Documents\AI Lasagne Generator\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\certifi\*"; DestDir: "{app}\certifi"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\User\Documents\AI Lasagne Generator\charset_normalizer\*"; DestDir: "{app}\charset_normalizer"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\User\Documents\AI Lasagne Generator\cryptography\*"; DestDir: "{app}\cryptography"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\User\Documents\AI Lasagne Generator\cryptography-41.0.7.dist-info\*"; DestDir: "{app}\cryptography-41.0.7.dist-info"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\User\Documents\AI Lasagne Generator\imgs\*"; DestDir: "{app}\imgs"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\User\Documents\AI Lasagne Generator\importlib_metadata-7.0.1.dist-info\*"; DestDir: "{app}\importlib_metadata-7.0.1.dist-info"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\User\Documents\AI Lasagne Generator\keyring-24.3.0.dist-info\*"; DestDir: "{app}\keyring-24.3.0.dist-info"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\User\Documents\AI Lasagne Generator\PIL\*"; DestDir: "{app}\PIL"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\User\Documents\AI Lasagne Generator\tcl\*"; DestDir: "{app}\tcl"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\User\Documents\AI Lasagne Generator\tcl8\*"; DestDir: "{app}\tcl8"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\User\Documents\AI Lasagne Generator\tk\*"; DestDir: "{app}\tk"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\User\Documents\AI Lasagne Generator\wheel-0.41.2.dist-info\*"; DestDir: "{app}\wheel-0.41.2.dist-info"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\User\Documents\AI Lasagne Generator\zstandard\*"; DestDir: "{app}\zstandard"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\User\Documents\AI Lasagne Generator\_asyncio.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\_bz2.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\_cffi_backend.cp311-win_amd64.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\_ctypes.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\_decimal.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\_elementtree.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\_hashlib.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\_lzma.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\_multiprocessing.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\_overlapped.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\_queue.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\_socket.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\_ssl.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\_tkinter.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-console-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-datetime-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-debug-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-errorhandling-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-file-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-file-l1-2-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-file-l2-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-handle-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-heap-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-interlocked-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-libraryloader-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-localization-l1-2-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-memory-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-namedpipe-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-processenvironment-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-processthreads-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-processthreads-l1-1-1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-profile-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-rtlsupport-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-string-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-synch-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-synch-l1-2-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-sysinfo-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-timezone-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-core-util-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-crt-conio-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-crt-convert-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-crt-environment-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-crt-filesystem-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-crt-heap-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-crt-locale-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-crt-math-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-crt-process-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-crt-runtime-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-crt-stdio-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-crt-string-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-crt-time-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\api-ms-win-crt-utility-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\base_library.zip"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\libcrypto-3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\libffi-8.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\libssl-3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\pyexpat.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\python3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\python311.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\select.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\tcl86t.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\tk86t.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\ucrtbase.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\unicodedata.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Documents\AI Lasagne Generator\VCRUNTIME140.dll"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

