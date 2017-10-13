//
// Created by 100514971 on 10/13/2017.
//

#using <System.dll>

using namespace System;
using namespace System::IO::Ports;
using namespace System::Threading;

public ref class ArduinoCom
{
private:
    static bool _continue;
    static SerialPort^ _serialPort;

public:
    static void Main()
    {

        String^ message;
        StringComparer^ stringComparer = StringComparer::OrdinalIgnoreCase;
        Thread^ readThread = gcnew Thread(gcnew ThreadStart(ArduinoCom::Read));

        // Create a new SerialPort object with default settings.
        _serialPort = gcnew SerialPort();

        // These are the Arduino com defaults.
        _serialPort->PortName = SetPortName(_serialPort->PortName);
        _serialPort->BaudRate = 9600;
        _serialPort->Parity = Parity::None;
        _serialPort->DataBits = 8;
        _serialPort->StopBits = StopBits::One;
        _serialPort->Handshake = Handshake::None;

        // Set the read/write timeouts
        _serialPort->ReadTimeout = 500;
        _serialPort->WriteTimeout = 500;

        _serialPort->Open();
        _continue = true;
        readThread->Start();

        Console::WriteLine("Type BYE to exit");

        while (_continue)
        {
            message = Console::ReadLine();

            if (stringComparer->Equals("bye", message))
            {
                _continue = false;
            }
            else
            {
                _serialPort->WriteLine(
                        String::Format("{0}",message) );
            }
        }

        readThread->Join();
        _serialPort->Close();
    }

    static void Read()
    {
        while (_continue)
        {
            try
            {
                String^ message = _serialPort->ReadLine();
                Console::WriteLine(message);
            }
            catch (TimeoutException ^) { }
        }
    }

    static String^ SetPortName(String^ defaultPortName)
    {
        String^ portName;

        Console::WriteLine("Available Ports:");
        for each (String^ s in SerialPort::GetPortNames())
        {
            Console::WriteLine("   {0}", s);
        }

        Console::Write("COM port({0}): ", defaultPortName);
        portName = Console::ReadLine();

        if (portName == "")
        {
            portName = defaultPortName;
        }
        return portName;
    }


};

int main()
{
    ArduinoCom::Main();
}