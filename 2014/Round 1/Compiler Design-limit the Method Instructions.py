for _ in range(int(input())):
	stk = []
	s = input()
	instr = 0
	error = False
	insideFunction = False
	mainOccurred = False
	for i in range(len(s)):
		if s[0] != '{':
			error = True
			break
		elif s[1] != '<':
			error = True
			break
		else:
			if s[i] == '{' and i == 0:
				stk.append(s[i])
			elif (s[i] == '{' and i != 0) and (stk[-1] == '<' or stk[-1] == '('):
				stk.append(s[i])
			elif s[i] == '(' and insideFunction == False:
				stk.append(s[i])
				insideFunction = True
			elif s[i] == '<' and mainOccurred == False:
				stk.append(s[i])
			elif s[i] == ')' and len(stk) != 0 and stk[-1] == '(':
				stk.pop()
			elif s[i] == '}' and len(stk) != 0 and stk[-1] == '{':
				stk.pop()
			elif s[i] == '>' and len(stk) != 0 and stk[-1] == '<':
				stk.pop()
				mainOccurred = True
			elif s[i] == 'P' and instr <= 100:
				instr+=1
				continue
			else:
				error = True
				break
	if len(stk) != 0:
		error = True
	if error:
		print('Compilation Errors')
	else:
		print('No Compilation Errors')

			