def txt_writer(write):
    f=open('text/text.txt','w')
    f.writelines(write)
    f.close()

write=['H','E','L','L','O',' ','W','O','R','L','D','!','!','!']
txt_writer(write)