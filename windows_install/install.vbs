Set fso = CreateObject("Scripting.FileSystemObject")

Set oShell = CreateObject("WScript.Shell")

userpath = oShell.ExpandEnvironmentStrings("%USERPROFILE%")

tmppath = "C:\tmp"

maketmp = "cmd /K cd C:\ & mkdir " & tmppath
maketmp = maketmp & " & exit"

If NOT fso.FolderExists(tmppath) Then
	oShell.Run maketmp
End If	