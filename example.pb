Func MainLoop(prefix) -> prefix + " Loop!!"

Func join(elements, separator)
	Set result = ""
	Set len = LEN(elements)

	For i = 0 To len Then
		Set result = result + elements/i
		If i != len - 1 Then Set result = result + separator
	End

	Return result
End

Func map(elements, func)
	Set new_elements = []

	For i = 0 To LEN(elements) Then
		APPEND(new_elements, func(elements/i))
	End

	Return new_elements
End

Print("Hello World!!")

For i = 0 To 5 Then
	Print(join(map(["First", "Second"], MainLoop), ", "))
End
