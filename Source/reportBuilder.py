from company import Company

import json

class ReportBuilder():
    def __init__(self, company: Company) -> None:
        with open('settings.json', encoding='utf-8') as file:
            self.settings = json.load(file)
        
        self.company = company
        self.ok = self.settings['visual.symbol.ok'] + '\n'
        self.bad = self.settings['visual.symbol.bad'] + '\n'
        
    
    def getReport(self) -> str:
        company = self.company
        
        text  = 'Отчёт о компании:' + '\n' * 2
        text += 'Тип компании: ' + self.bold(company.companyType) + '\n'
        text += 'ИНН: ' + self.script(company.inn) + '\n'
        text += 'ОГРН: ' + self.script(company.ogrn) + '\n'*2
        
        if len(company.positiveDict) > 0:
            text += 'Позитив:' + '\n'
            positive = ''
            text += self.addPositiveToText(positive)
            
        if len(company.negativeDict) > 0:
            text += 'Негатив:' + '\n'
            negative = ''
            text += self.addNegativeToText(negative)
        
        
        return text
    
    
    def addPositiveToText(self, text: str) -> str:
        company = self.company
        
        if company.positiveLicensees:
            text += f'-Наличие лицензий: {self.ok}'
        
        if company.companyType == 'ЮЛ':
            if company.positiveBranches:
                text += f'-Наличие филиалов: {self.ok}'
        
            if company.positiveCapital:
                text += f'-Уставный капитал более 50.000 рублей: {self.ok}'

        
        text += '-Компания находится в реестре МСП: '
        text += self.ok if company.positiveIsInMSP else self.bad
        
        if company.positiveIsInMSP:
            text += '--Дата включения в МСП: ' + self.bold(company.mspInclusionDate) + '\n'
            text += '--Категория субъекта МСП: ' + self.bold(company.mspSubjectCategory) + '\n'
            text += '--Недавно создана: ' + self.bold(company.mspRecreated) + '\n'
            text += '--Социальное предприятие: ' + self.bold(company.mspSocial) + '\n'
            text += '--Среднесписочная численность работников: ' + self.bold(company.mspWorkers) + '\n'
            text += '--Дата состояния: ' + self.bold(company.mspInstanceDate)
            
            if company.companyType == 'ИП':
                text += '--Адрес предприятия: ' + self.bold(company.mspAddress) + '\n'
        
        return text + '\n'
    
    
    def addNegativeToText(self, text: str) -> str:
        company = self.company
        negativeList = [x for x in dir(company) 
                        if 'negative' in x 
                        and x != 'negativeDict' 
                        and x != 'negativeStatus'
                        ]
        print(negativeList)
        
        for i in negativeList:
            if getattr(company, i):
             text = self.checkAndAdd(text, company.negDescription[i])
             
        text += '-Статус: ' + self.bold(company.negativeStatus)       
        
        return text
    
    
    def checkAndAdd(self, source: str, description: str) -> str:
        try:
            source += '-' + self.bold(description) + '\n'
        except:
            pass
        
        return source
    
    
    def bold(self, text: str) -> str:
        return f'<b>{text}</b>'


    def script(self, text: str) -> str:
        return f'<code>{text}</code>'