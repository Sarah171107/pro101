import dropbox
class TransferData: 
    def _init_ (self,accesstoken):
        self.accesstoken=accesstoken
    def uploadfile(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.accesstoken)
        f=open(filefrom,'rb')
        dbx.fileupload(f.read(),fileto)   
        
        
def main():
    accesstoken='sl.A-FTwmSVbm4cPESo3ApKSc2hwkn9fnc-PH6VNeslaPYTXJNBNdW0l_CXB6zvcUIZ2M1m-UuCULOgL9Vs2cV3E9S9Ov-meYfR8AZoVALd6GTjHeDH1zh-5skw5KsUddQL86iYr5Y'
    transferData =TransferData(accesstoken)
    filefrom='C:/Users/Hp/Downloads/class97 coding/empty.txt'
    fileto='C:/Users/Hp/Dropbox'
    transferData.uploadfile (filefrom,fileto)
    print('file has been moved')      
    
main()    