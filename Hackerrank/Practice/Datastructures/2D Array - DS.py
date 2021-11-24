def hourglasss(arr):
    maxsum  = -99 # anything less than -63 is fine
    for i in range(4):
        for j in range(4):

            top = sum(arr[i][j:j+3])
            mid = arr[i+1][j+1]
            bot = sum(arr[i+2][j:j+3])

            hourglassz = top+mid+bot
            maxsum = max(hourglassz,maxsum)
    return maxsum

