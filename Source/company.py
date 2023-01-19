from dataclasses import dataclass

@dataclass()
class Company:
    inn: str
    ogrn: str
    companyType: str
    negativeDict: dict 
    positiveDict: dict
    registryDict: dict
        
    mspInclusionDate: str
    mspSubjectCategory: str
    mspRecreated: str
    mspSocial: str
    mspWorkers: str
    mspInstanceDate: str
    mspAddress: str
    
    # Общие
    negativeNewCompany: bool
    negativeMassManager: bool
    negativeMassFounder: bool
    
    # ЮЛ
    negativeArrears: bool
    negativeDisqualifiedInside: bool
    negativeDisqualifiedOutside: bool
    negativeDisqualifiedSameID: bool
    negativeMassAddressReg: bool
    negativeMassAddressFns: bool
    negativeChangeAddress: bool
    negativeFalseAddress: bool
    negativeChangeRegion: bool
    negativeMassManagerFalseID: bool
    negativeBadManager: bool
    negativeMassManagerFounderReg: bool
    negativeDisqualifiedFounderOutside: bool
    negativeDisqualifiedFounderOutsideFalseID: bool
    negativeFounderClosed: bool
    negativeFounderClosedFalseInn: bool
    negativeChangeManagerFounder: bool
    negativeOnlyFounder: bool
    negativeEncum: bool
    negativeNoReport: bool
    negativeDebt: bool
    negativeDecreaseCapital: bool
    negativeTaskCheckRisk: bool
    negativeExcluded: bool
    
    negativeStatus: str = ''
        
    positiveLicensees: bool = False
    positiveBranches: bool = False
    positiveCapital: bool = False
    positiveIsInMSP: bool = False
    
    negDescription = {
        'negativeNewCompany': 'Организация зарегистрирована недавно',
        'negativeMassManager': 'Руководитель назначен главой 5 или более организаций',
        'negativeMassFounder': 'Учредитель находится в реестре массовых учредителей',
        'negativeDisqualifiedInside': 'Руководитель дисквалифицирован в данной организации',
        'negativeDisqualifiedOutside': 'Руководитель дисквалифицирован в других организациях',
        'negativeDisqualifiedSameID': 'Руководитель с данными ФИО без указанного ИНН дисквалифицирован в других организациях',
        'negativeMassAddressReg': 'Организация зарегистрирована по адресу массовой регистрации (по данным ФНС)',
        'negativeMassAddressFns': 'Организация зарегистрирована по адресу массовой регистрации (более 9 организаций по данным ФНС)',
        'negativeChangeAddress': 'Организация приняла решение изменить адрес',
        'negativeFalseAddress': 'Адрес организации недостоверный (по данным ФНС)',
        'negativeChangeRegion': 'За последний год регион организации был изменен',
        'negativeMassManagerFalseID': 'Руководитель с данными ФИО без указанного ИНН руководит боле чем 5 организациями',
        'negativeBadManager': 'Руководитель признан ФНС недостоверным',
        'negativeMassManagerFounderReg': 'Учредитель организации находится в реестре массовых руководителей',
        'negativeDisqualifiedFounderOutside': 'Учредитель дисквалифицирован как руководитель в других организациях',
        'negativeDisqualifiedFounderOutsideFalseID': 'Учредитель с данным ФИО без указанного ИНН дисквалифицирован как руководитель в других организациях',
        'negativeFounderClosed': 'Учредитель ранее участвовал более чем в 3-х ликвидированных компаниях',
        'negativeFounderClosedFalseInn': 'Учредитель с данным ФИО без указанного ИНН ранее участвовал более чем в 3 ликвидированных компаниях',
        'negativeChangeManagerFounder': 'В организации была одновременная смена руководителя и учредителя в течение года',
        'negativeOnlyFounder': 'Руководитель компании является единственным учредителем исключительно только в этой компании',
        'negativeEncum': 'Имеются обременения доли любого действующего учредителя в УК',
        'negativeNoReport': 'Организация не представляет налоговую отчетность более года',
        'negativeDebt': 'Организация имеет задолженность по уплате налогов более 1000 руб.',
        'negativeDecreaseCapital': 'Организация приняла решение об уменьшении уставного капитала',
        'negativeTaskCheckRisk': 'Организация имеет высокий риск налоговой проверки',
        'negativeExcluded': 'Организация исключена из реестра МСП',
        'negativeArrears': 'Организация имеет недоимки по уплате налогов',
        'negativeAccountBlocked': 'Организация имеет заблокированный счет в банке',
        'negativeBankrupt': 'Организация подала заявление о банкротстве'
    }
    
    isUL: bool = False
    isIP: bool = False