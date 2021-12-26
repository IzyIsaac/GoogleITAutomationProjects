#!/usr/bin/env python3
import os
import sys
from datetime import date
import reports
import emails

def main(argv):
    descriptions_dir = 'supplier-data/descriptions/'
    out_file = '/tmp/processed.pdf'
    descriptions = []
    for filename in os.listdir(descriptions_dir):
        with open(os.path.join(descriptions_dir, filename)) as f:
            description = {}
            # Read title
            description['name'] = f.readline().strip()
            # Read name
            description['weight'] = int(f.readline().split(' ')[0])
            descriptions.append(description)
    print("generated report...")
    reports.generate_report(out_file, f'Processed update on {date.today()}', descriptions)
    emails.generate('automation@example.com', 'student-00-405db269f197@example.com', 
        'Upload Completed - Online Fruit Store', 
        'All fruits are uploaded to our website successfully. A detailed list is attached to this email.',
        out_file)
    emails.send()
        
if __name__ == "__main__":
    main(sys.argv)