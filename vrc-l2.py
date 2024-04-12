from pymodbus.client.sync import ModbusSerialClient as ModbusClient

client = ModbusClient(method='RTU', port='COM3', bytesize=8, stopbits=1, baudrate=9600, slave=1, parity='N', strict=False)
connection = client.connect()
if connection is True:
    print("Modbus Connection Successful")

dimmer=client.read_holding_registers(0x0001, 6, unit=1)
print(dimmer.registers)

dimmer1=client.write_register(0x0004, 0xFF08, unit=1)


client.close()