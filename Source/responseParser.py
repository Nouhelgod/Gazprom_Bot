from company import Company
from reportBuilder import ReportBuilder as reporter
import requests
import json

class Response:
    def __init__(self, code):
        with open('settings.json', encoding='utf-8') as file:
            self.settings = json.load(file)
        
        self.company = Company
        
        self.code = code
        self.keyFns = self.settings['api.key.fns']
        self.keyZakupki = self.settings['api.key.zakupki']
        self.fnsResponse = self.requestFNS('check')
        
        self.company.isIP = self.checkForCompanyType()
        self.company.isUL = not self.company.isIP
                  
        self.company.negativeDict = self.getPros('Негатив')
        self.company.positiveDict = self.getPros('Позитив')

        self.company.inn = self.parseInn(fl = self.company.isIP)
        self.company.ogrn = self.parseOgrn(fl = self.company.isIP)
        
        self.parsePositive()
        self.parseNegative()
                
        
    def requestFNS(self, method: str) -> str:
            fnsResponse = requests.get(
                self.settings['api.url.fns'] + method +
                f'?req={self.code}' +
                f'&key={self.keyFns}'
            ).text
            return json.loads(fnsResponse)['items'][0]
    
            
    def checkForCompanyType(self) -> bool:
        if 'ИП' in self.fnsResponse:
            self.company.companyType = 'ИП'
            
        else:
            self.company.companyType = 'ЮЛ'
            return False
        
        return True
        
    
    def getPros(self, pros: str) -> dict:
        return self.fnsResponse[self.company.companyType][pros]
        
        
    def parseInn(self, fl: bool) -> str:
        keyword = 'ИНН'
        category = 'ЮЛ'
        if fl:
            keyword += 'ФЛ'
            category = 'ИП'
        
        return self.fnsResponse[category][keyword]
    
    
    def parseOgrn(self, fl: bool) -> str:
        keyword = 'ОГРН'
        category = 'ЮЛ'
        if fl:
            keyword += 'ИП'
            category = 'ИП'
        
        return self.fnsResponse[category][keyword]
    
    
    def parsePositive(self):
        company = self.company
        category = 'Позитив'
        
        company.positiveLicensees = self.checkProsFor(category, 'Лицензии')
        company.positiveBranches = self.checkProsFor(category, 'Филиалы')
        company.positiveCapital = self.checkProsFor(category, 'КапБолее50тыс')
        company.positiveIsInMSP = self.checkProsFor(category, 'РеестрМСП')
        
        if self.company.positiveIsInMSP:           
            self.company.registryDict = self.company.registryDict['РеестрМСП']
            self.parseMSP()
            

    def parseMSP(self):
        company = self.company
        
        company.mspInclusionDate = self.checkRegistryFor('ДатаВклМСП')
        company.mspSubjectCategory = self.checkRegistryFor('КатСубМСП')
        company.mspRecreated = self.checkRegistryFor('ПризНовМСП')
        company.mspSocial = self.checkRegistryFor('СведСоцПред')
        company.mspWorkers = self.checkRegistryFor('ССЧР')
        company.mspInstanceDate = self.checkRegistryFor('ДатаСост')
        company.mspAddress = self.checkRegistryFor('АдресМСП')
        
            
    def checkRegistryFor(self, field: str) -> str or None:
        registry = self.company.registryDict
        
        if field in registry:
            return registry[field]
        
        return None
    
    
    def parseNegative(self):
        company = self.company
        category = 'Негатив'
        
        # Общие
        company.negativeStatus = self.getPros('Негатив')['Статус']
        company.negativeExcluded = self.checkProsFor(category, 'ИсклИзРеестраМСП')
        company.negativeNewCompany = self.checkProsFor(category, 'РегНедавно')
        company.negativeMassManager = self.checkProsFor(category, 'РеестрМассРук')
        company.negativeMassFounder = self.checkProsFor(category, 'РеестрМассУчр')
        company.negativeAccountBlocked = self.checkProsFor(category, 'БлокСчета')
        company.negativeBankrupt = self.checkProsFor(category, 'Банкрот')
        
        #ЮЛ
        company.negativeArrears = self.checkProsFor(category, 'НедоимкаНалог')
        company.negativeDisqualifiedInside = self.checkProsFor(category, 'ДисквРук')
        company.negativeDisqualifiedOutside = self.checkProsFor(category, 'ДисквРукДр')
        company.negativeDisqualifiedSameID = self.checkProsFor(category, 'ДисквРукДрБезИНН')
        company.negativeMassAddressReg = self.checkProsFor(category, 'МассАдресс')
        company.negativeMassAddressFns = self.checkProsFor(category, 'РеестрМассАдрес')
        company.negativeChangeAddress = self.checkProsFor(category, 'РешИзмАдрес')
        company.negativeFalseAddress = self.checkProsFor(category, 'НедостоверАдрес')
        company.negativeChangeRegion = self.checkProsFor(category, 'СменаРег')
        company.negativeMassManagerFalseID = self.checkProsFor(category, 'МассРукБезИНН')
        company.negativeBadManager = self.checkProsFor(category, 'НедостоверРук')
        company.negativeMassManagerFounderReg = self.checkProsFor(category, 'РеестрМассРукУчр')
        company.negativeDisqualifiedFounderOutside = self.checkProsFor(category, 'ДисквУчрДр')
        company.negativeDisqualifiedFounderOutsideFalseID = self.checkProsFor(category, 'ДисквУчрДрБезИНН')
        company.negativeFounderClosed = self.checkProsFor(category, 'УчрЛиквКомп')
        company.negativeFounderClosedFalseInn = self.checkProsFor(category, 'УчрЛиквКомпБезИНН')
        company.negativeChangeManagerFounder = self.checkProsFor(category, 'ОдноврСменаРукУчр')
        company.negativeOnlyFounder = self.checkProsFor(category, 'РукУчр1Комп')
        company.negativeEncum = self.checkProsFor(category, 'Обременения')
        company.negativeNoReport = self.checkProsFor(category, 'НеПредостОтч')
        company.negativeDebt = self.checkProsFor(category, 'ЗадолжНалог')
        company.negativeDecreaseCapital = self.checkProsFor(category, 'РешУмКап')
        company.negativeTaskCheckRisk = self.checkProsFor(category, 'РискНалогПроверки')
        
    
    def checkProsFor(self, category: str, field: str) -> bool:
        if category == 'Позитив':
            targetDict = self.company.positiveDict
        
        else:
            targetDict = self.company.negativeDict
        
        if field in targetDict:
            return True

        return False
    
    
    def __str__(self) -> str:
        reportBuilder = reporter(self.company)
        text = reportBuilder.getReport()    
        return text
        
    
