import sys
import pickle
x_min = 0
y_min = 0
# get max height
y_max = int(sys.stdin.readline().strip())
# get max width
x_max = int(sys.stdin.readline().strip())

# print x_max, y_max
with open("mySavedDict.txt", "rb") as myFile:
    domain = pickle.load(myFile)

# print domain

sk_count = 0
x_y1 = []
x_y2 = []
x_ydiff = [0,0]
d_count = 0
diff_val = 4
# user input handling thread
events = ["moving diagonally, right up","moving diagonally, left up", "moving diagonally, right down", "moving diagonally, left down", "moving right", "moving left", "moving up", "moving down","idle"]
ev_seq = [-1]

# peron's current position
cur_pos = -1

# person's current trajectory
cur_traj = (-1,-1)

def check_proximity(x,y):
	for el in domain:
		if (x > el['x']-10 and x < el['x']+10) and (y > el['y']-10 and y < el['y']+10):
			return domain.index(el)
	return -1		

def trajectory(p,x_y):
	# targets
	xt = p[0]
	yt = p[1]
	# source
	xs = p[0]
	ys = p[1]

	t=-1
	s=-1
	while( (x_min<=xt<=x_max) and (y_min<=yt<= y_max) and t == -1 ):
		# to - dest
		xt += x_ydiff[0]
		yt += x_ydiff[1]			
		t = check_proximity(xt,yt)
		
	while( (x_min<=xs<=x_max) and (y_min<=ys<= y_max) and s == -1 ):
		# to source
		xs -= x_ydiff[0]
		ys -= x_ydiff[1]
		s = check_proximity(xs, ys)

	if t != -1 and s != -1 and t!=s:
		return (t,s)
		
	else:
		return (-1,-1)



while True:
	data = sys.stdin.readline().strip()
	if data == "":
		break

	x = data.split()
	if len(x) > 1:
		if sk_count <= 4:

			cur_per = "Person 1"

			# GETTING CURRENT CO-ORDINATES
			x_y2 = [int(x[2]),int(x[3])]

			# CHECKING THE POSITION OF THE PERSON RELATIVE TO THE DOMAIN
			pos = check_proximity(x_y2[0],x_y2[1])
			if pos != -1 and pos != cur_pos:
				sys.stdout.write(cur_per+" at " + domain[pos]['name']+"\n")
				cur_pos = pos
			
			# CALCULATING THE DIFFERENCE IN MOVEMENT AND DETERMINE THE DIRECTION
			x_ydiff[0] +=  x_y2[0]-x_y1[0]
			x_ydiff[1] +=  x_y2[1]-x_y1[1]
			d_count += 1
			if d_count == 3:
				seq_el = -1
				if x_ydiff[0] > diff_val and x_ydiff[1] > diff_val:
					seq_el = 0
				elif x_ydiff[0] < -diff_val and x_ydiff[1] > diff_val:
					seq_el = 1
				if x_ydiff[0] > diff_val and x_ydiff[1] < -diff_val:
					seq_el = 2
				elif x_ydiff[0] < -diff_val and x_ydiff[1] < -diff_val:
					seq_el = 3					
				elif x_ydiff[0] > diff_val :
					seq_el = 4
				elif x_ydiff[0] < -diff_val:
					seq_el = 5					
				elif x_ydiff[1] > diff_val :
					seq_el = 6
				elif x_ydiff[1] < -diff_val:
					seq_el = 7
				else:
					seq_el = -1
				# PRINTING DIRECTION
				if seq_el != ev_seq[-1] and seq_el != -1:
					ev_seq.append(seq_el)
					sys.stdout.write(cur_per+" direction "+events[seq_el]+"\n")

				# CALCULATING PREDICTED TRAJECTORY
				traj = trajectory(x_y2,x_ydiff)
				if traj != (-1,-1) and traj != cur_traj:
					sys.stdout.write(cur_per + " moving From " + domain[traj[1]]['name'] + ", towards " + domain[traj[0]]['name']+"\n")
					cur_traj = traj

				x_ydiff = [0,0]
				d_count = 0
				
			x_y1 = [int(x[2]),int(x[3])]
			sk_count = 0
		else:
			x_y1 = [int(x[2]),int(x[3])]
			sk_count = 0

	else:
		sk_count += 1

	sys.stdout.flush()

