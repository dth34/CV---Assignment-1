import cv2
import time

cap = cv2.VideoCapture(0)

while(True):
    tic = time.perf_counter()
# Get image
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 640x480
    toc = time.perf_counter()
    #t1 = toc-tic
    #print('t1 = ' + str(t1))
# Brightest pixel using OpenCV
    #min_val, max_val, min_index, max_index = cv2.minMaxLoc(gray)
    # Draw point on brightest pixel
    #gray = cv2.circle(gray, max_index, radius=10, color=(255, 255, 255), thickness=-1)
    #toc = time.perf_counter()
    #t2 = toc-tic
    #print('t2 = ' + str(t2))
# Redness evaluation
    #red = frame[:,:,2]
    #min_rval, max_rval, min_rindex, max_rindex = cv2.minMaxLoc(red) 
    # Draw point on reddest pixel
    #gray = cv2.circle(gray, max_rindex, radius=10, color=(255, 255, 255), thickness=-1)

# Loop Method
# Brightest pixel
    xmax = 0
    ymax = 0
    maxLoopVal = 0
    for i in range(0,480):
        for j in range(0,640):            
           if gray[i,j] > maxLoopVal:
               maxLoopVal = gray[i,j]
               ymax = i
               xmax = j  
    gray = cv2.circle(gray, (xmax,ymax), radius=10, color=(0, 255, 255), thickness=-1) 

# Reddest pixel
#   red = frame[:,:,2]
#    xrmax = 0
#    yrmax = 0
#    maxrLoopVal = 0
#    for i in range(0,480):
#        for j in range(0,640):            
#            if red[i,j] > maxrLoopVal:
#                maxrLoopVal = red[i,j]
#                yrmax = i
#                xrmax = j  
    #gray = cv2.circle(gray, (xrmax,yrmax), radius=10, color=(0, 255, 255), thickness=-1) 
# Time measure
    toc = time.perf_counter()
    t = toc-tic
    fps = str(int(1/t))
# Text over image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(gray, fps + ' FPS', (400, 450), font, 2, (255, 255, 255), 3, cv2.LINE_4)
# Show image
    cv2.imshow('frame',gray)
    toc = time.perf_counter()
    t1 = toc-tic
    print('t1 = ' + str(t1))
# Close frame 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()