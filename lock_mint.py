from pymodbus.client.sync import ModbusSerialClient as ModbusClient

client = ModbusClient(method='RTU', port='COM3', bytesize=8, stopbits=1, baudrate=115200, slave=1, parity='N')
connection = client.connect()
print(connection)
lock=client.read_holding_registers(1010, 1, slave=1)
print(lock)
lock1=client.write_register(1004, 2048, slave=1)



