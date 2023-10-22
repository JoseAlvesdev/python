class Computador:
    def __init__(
        self, 
        monitor, 
        cpu, 
        gpu, 
        mouse, teclado, 
        memoria_ram, 
        motherboard
    ):
        self.monitor = monitor
        self.cpu = cpu
        self.gpu = gpu
        self.mouse = mouse
        self.teclado = teclado
        self.memoria_ram = memoria_ram
        self.motherboard = motherboard

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    

class MeuSetup(Computador):
    def __init__(self, gamepad, hub_usb, **kwargs):
        self.gamepad = gamepad
        self.hub_usb = hub_usb
        super().__init__(**kwargs)


MeuSetup = MeuSetup(
    monitor='Dell 27 Pol. 165hz IPS',
    cpu='AMD Ryzen 7 3800x',
    gpu='NVIDEA RTX 3080 TI Zotac',
    mouse='LOGITECH G305 Hero 12000DPI',
    teclado='GAMAKAY PRO',
    memoria_ram='HYPERX Fury 16GB 2x8 3200Mhz',
    motherboard='GIGABYTE Aorus B550 Elite',
    gamepad='MICROSOFT DualShock Xbox Series S',
    hub_usb='HubUsb 10 portas'
)

print(MeuSetup)