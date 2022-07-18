import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_to,file_from):
        dbx = dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read() , file_to)


def main():
    access_token='sl.BKqqQv7WW_YFpk9kkzuRmhPh5fitwfmfucgB0MM2S9LMImECt3VBAqlhNKQTPsOi0TX7vTrU8tBlsWqdjlqSlsaDDN4JaFMYqweOR-4UvNGQ3RY5xIz2RK4QkcqcBliQhjEF9Ez1XU6U' 
    transferData= TransferData(access_token)



    file_from=input("Enter the file path to transfer: ")
    file_to  =input("enter the file path to upload to dropbox: ")


    transferData.upload_file(file_to,file_from)
    print("file has been moved !!")

main()