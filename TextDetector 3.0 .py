import boto3
import os.path
import csv

def detect_text(photo, bucket):

#Import list from S3 
    session = boto3.Session( 
         aws_access_key_id='AKIASNW4ZVYG55YF4UPB', 
         aws_secret_access_key='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')


#Then use the session to get the resource
    s3 = session.resource('s3')

    my_bucket = s3.Bucket('rekognitiontextdetector')

    for my_bucket_object in my_bucket.objects.all():
   
        directory = "./"
        output = my_bucket_object.key + ".txt" # tu tworzy nazwe pliku 
        file_path = os.path.join(directory,output)
        if not os.path.isdir(directory):
                    os.mkdir(directory)
        outfile = open(file_path, 'w',encoding="utf-8")

        client=boto3.client('rekognition')
        response=client.detect_text(Image={'S3Object':{'Bucket':'rekognitiontextdetector','Name': my_bucket_object.key}}) 
        textDetections=response['TextDetections']
        print ('Detected text\n----------')
        for text in textDetections: # tu jest tworzona zawartosc pliku 
                        print ('Detected text:' + text['DetectedText'], file = outfile)
                        print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%", file = outfile)
                        print(file = outfile)
        
         
        outfile.close()
    

def main():
    
    bucket='bucket'
    photo='photo'
    text_count=detect_text(photo,bucket)
    print("Text detected: " + str(text_count), )
    

if __name__ == "__main__":
    main()

    
