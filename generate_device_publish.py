from device import device
qtd_devices = int(input("Digite quantos devices voceŝ deseja: "))
devices = [0] * qtd_devices
device_send_amount = int(input("Digite quantidade de transmissões: "))

print("Serão criados %s que irão enviar %s registros." %(len(devices), device_send_amount))


count = 0

while count < len(devices):

    devices[count] = "Device "+str(count)

    randon_topic = "/home/"+devices[count]
    
    print(devices[count])
    print(randon_topic)

    device_name = device(devices[count], devices[count], randon_topic, "localhost")
    device_name.send(device_send_amount)
  
    count += 1

    