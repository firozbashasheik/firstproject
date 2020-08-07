def lead_splitting(lead_list):
    lead_name= {}
    lead_count= {}
    if lead_list:
        for leads in lead_list:
            if '@' in leads:
                company = leads.split ('@')[1]
                if lead_name.get(company):
                    lead_name[company].append(leads)
                else:
                    lead_name[company]=[leads]
            else:
                print('enter correct lead',leads)
        
        for name, count in lead_name.items():
            lead_count[name] = len(count)
    return lead_name, lead_count
    
#driver code
lead_list=['hello@dhruvsoft.com','john@dhruvsoft.com','bob@google.com', 'alice@amazon.com','william@salesforce.com', 'jhon@heroku.com','chiru@nestuite.com', 'venky@dhruvsoftcom', 'naveen@zoho.com', 'doe@zoho.com','aws@dhruvsoft.com','rgv@sivio.com','pawan@netsuite.com','welcome@dhruvsoft.com']
print(lead_splitting(lead_list))