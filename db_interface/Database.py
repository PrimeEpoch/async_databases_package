from typing import Optional
from abc import ABC

class Database(ABC):
  
  def __init__(self,
               username: Optional[str] = None,
               password: Optional[str] = None,
               host_addr: Optional[str] = None,
               host_port: Optional[int] = None,
              ):
    self.username = username
    self.password = password
    self.host_addr = host_addr
    self.host_port = host_port
