


import re




pattern = re.compile(r'^(BASH|BRAINFUCK|C(LISP|LOJURE|PP|SHARP)?|D(ART)?|ERLANG|GO|GROOVY|HASKELL|JAVA(SCRIPT)?|LUA|OBJECTIVEC|OCAML|PASCAL|PERL|PHP|PYTHON|R(UBY)?|SBCL|SCALA)$')



for _ in range(int(input())):
    print('VALID' if re.match(pattern, input().split()[1]) else 'INVALID')
