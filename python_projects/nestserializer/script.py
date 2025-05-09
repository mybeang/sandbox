import random
from app.models import ChargeCodeModel, BillingModel
from datetime import datetime
import calendar


min_daily_records = 100000
max_daily_records = 200000
min_usage_amount = 10.0
max_usage_amount = 100.0
min_cost = 0.0
max_cost = 100.0
min_cost_discount = 0.83
max_cost_discount = 1
min_credit_discount = -10.0
max_credit_discount = 0


invoice_months = ['2024/0%d' % i for i in range(1, 10)]
accounts = [c.account_id for c in ChargeCodeModel.objects.filter()]
products = [
    {
        "name": 'EC2 VM',
        "services": {
            "names": ['instance', 'cpu', 'memory'],
            "weights": [0.4, 0.3, 0.3] 
        }
    }, {
        "name": 'S3',
        "services": {
            "names": ['hot', 'warn', 'cold'],
            "weights": [0.5, 0.3, 0.2] 
        }
    }, {
        "name": 'EC2 VPC',
        "services": {
            "names": ['nic', 'elastic ip', 'route', 'private-line'],
            "weights": [0.5, 0.2, 0.1, 0.2] 
        }
    }, {
        "name": 'Transit Gateway',
        "services": {
            "names": ['north-south', 'east-west'],
            "weights": [0.8, 0.2] 
        }
    }, {
        "name": 'Loadbalancer',
        "services": {
            "names": ['elb', 'alb'],
            "weights": [0.6, 0.4] 
        }
    }, {
        "name": 'Kubernetes',
        "services": {
            "names": ['elk1', 'elk2', 'elk2-2'],
            "weights": [0.5, 0.3, 0.2] 
        }
    }, {
        "name": 'Lambda',
        "services": {
            "names": ['faas', 'laas', 'ssss'],
            "weights": [0.8, 0.1, 0.1] 
        }
    }
]
projects_weight = [0.3, 0.3, 0.2, 0.1, 0.05, 0.03, 0.02]


def make_data_func(month, day):
    product = random.choices(products, weights=projects_weight)[0]
    service = random.choices(product['services']['names'], weights=product['services']['weights'])[0]
    return {
        "account_id": random.choice(accounts),
        "invoice_month": "".join(month.split('/')),
        "product_name": product['name'],
        "service_name": service,
        "usage_date": datetime(int(month.split('/')[0]), int(month.split('/')[1]), int(day), random.randrange(0, 24)),
        "usage_amount": random.uniform(min_usage_amount, max_usage_amount),
        "cost": random.uniform(min_cost, max_cost),
        "cost_discount": random.uniform(min_cost_discount, max_cost_discount),
        "credit_discount": random.uniform(min_credit_discount, max_credit_discount)
    }


def main():    
    for month in invoice_months:    
        _, end_date = calendar.monthrange(int(month.split('/')[0]), int(month.split('/')[1]))
        for day in range(1, int(end_date) + 1):            
            print(f"{month}/{day}")
            for _ in range(random.randrange(min_daily_records, max_daily_records)):
                BillingModel(**make_data_func(month, day)).save()
        
main()
