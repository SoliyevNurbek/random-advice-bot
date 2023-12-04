import requests


class Bored:
    def __init__(self) -> None:
        self.url = 'http://www.boredapi.com/api/'

    def get_activity(self) -> str:
        '''get activity from bored
        
        Returns:
            str: text of activity
        '''
        endpoint='activity/'
        url=self.url+endpoint
        response=requests.get(url)
        if response.status_code==200:
            return response.content.decode()
        return response.status_code

    def get_activity_by_type(self, type: str) -> dict:
        '''get activity by type

        Note:
            Type of the activity: ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"]
        
        Args:
            type (str): type
        
        Returns:
            dict: activity data
        '''
        endpoint='activity/'
        url=self.url+endpoint
        type={
            "type":type
        }
        response=requests.get(url,type)
        if response.status_code==200:
            return response.json()
        return response.status_code

    def get_activity_by_id(self, key: int) -> dict:
        '''get activity by key

        Note:
            A unique numeric id: [1000000, ..., 9999999]
        
        Args:
            key (int): key
        
        Returns:
            dict: activity data
        '''
        if key>=1000000 and key<=9999999:
            key={"key":key}
            endpoint='activity/'
            url=self.url+endpoint
            
            response=requests.get(url,key)
            if response.status_code==200:
                return response.json()
            return response.status_code
        else:
            print("Error")
        

    def get_activity_by_accessibility(self, accessibility: float) -> dict:
        '''get activity by accessibility

        Note:
            A factor describing how possible an event is to do with zero being the most accessible
            [0.0, ..., 1.0]
        
        Args:
            accessibility (float): accessibility
        
        Returns:
            dict: activity data
        '''
        if accessibility>=0.0 and accessibility<=1.0:
            accessibility={"accessibility":accessibility}
            endpoint='activity/'
            url=self.url+endpoint
            
            response=requests.get(url,accessibility)
            if response.status_code==200:
                return response.json()
            return response.status_code
        else:
            print("Error")

    def get_activity_by_price(self, price: float) -> dict:
        '''get activity by price

        Note:
            A factor describing the cost of the event with zero being free
            [0, 1]
        
        Args:
            price (float): price
        
        Returns:
            dict: activity data
        '''
        if price>=0 and price<=1:
            payload={"price":price}
            endpoint='activity/'
            url=self.url+endpoint
            
            response=requests.get(url,price=payload)
            if response.status_code==200:
                return response.json()
            return response.status_code
        else:
            print("Error")

    def get_activity_by_price_range(self, minprice: float, maxprice: float) -> dict:
        '''get activity by price

        Note:
            A factor describing the cost of the event with zero being free
            [0, 1]
        
        Args:
            minprice (float): min price
            maxprice (float): max price
        
        Returns:
            dict: activity data
        '''
        if minprice>=0 and minprice<=1 and maxprice>=0 and maxprice<=1:
            payload={"minprice":minprice,"maxprice":maxprice}
            endpoint='activity/'
            url=self.url+endpoint
            
            response=requests.get(url,params=payload)
            if response.status_code==200:
                return response.json()
            return response.status_code
        else:
            print("Error")