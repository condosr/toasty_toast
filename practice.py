import argparse
#import boto3
import os

parser = argparse.ArgumentParser()

#parser.add_argument("directory_name")
#parser.add_argument("customer")
#parser.add_argument()
#parser.add_argument()
#os.system('cmd /c' "mkdir practice")
#os.system('cmd /c' "cd practice")
#args = parser.parse_args()
#print(type(args.directory_name))
os.system(f'cmd /c "mkdir my_bones"')
#os.system(f'cmd /k "cd {args.directory_name} && aws s3 sync s3://restaurant-exports/{args.customer}/ . --profile {args.customer}"')
#os.system('cmd /k' "aws s3 sync s3://restaurant-exports/TheSmokehouseExportUser2/ . --profile toast")
#os.system('cmd /c' "aws s3 sync s3://restaurant-exports/TheSmokehouseExportUser2/ . --profile toast")