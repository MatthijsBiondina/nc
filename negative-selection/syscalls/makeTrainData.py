import subprocess

def chunks(filename,n):
	filestr = open(filename,'r').read()
	lines = filestr.split('\n')
	with open(filename + '.chunk','w+') as f:
		with open(filename + '.index','w+') as idx:
			for j, line in enumerate(lines):
				while len(line) <= n:
					line = line + ' '
				for i in range(n,len(line),n):
					f.write( line[i-n:i] + '\n' )
					idx.write(str(j) + '\n')

N = 50
chunks('snd-cert.train',N)
chunks('snd.test',N)
p = subprocess.Popen(('java -jar ../negsel2.jar -alphabet file://snd-cert/snd-cert.alpha -self snd-cert.train.chunk -n ' + str(N) + ' -r 3 -c -l < snd.test.chunk > test.scores').split())
p.wait()

		
