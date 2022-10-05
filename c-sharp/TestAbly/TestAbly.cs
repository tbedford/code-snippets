using System;
using System.Threading;
using IO.Ably;
using IO.Ably.Realtime;

// Uses https://github.com/tonerdo/dotnet-env

public class TestAbly
{
    public static void Main(string[] args)
    {
        Console.Out.WriteLine("Testing Ably...");

        DotNetEnv.Env.Load();
        var ably_key = DotNetEnv.Env.GetString("ABLY_API_KEY");
        var ably = new AblyRealtime(ably_key);
        
        ably.Connection.On(ConnectionEvent.Connecting, args =>
        {
            Console.Out.WriteLine("Connecting to Ably!");
        });

        ably.Connection.On(ConnectionEvent.Connected, args =>
        {
            Console.Out.WriteLine("Connected to Ably!");
        });

        ably.Connection.On(ConnectionEvent.Closed, args =>
        {
            Console.Out.WriteLine("Closed connection to Ably!");
        });

        var channel = ably.Channels.Get("ably-time-server");

        channel.Subscribe("event", message => {
            Console.Out.WriteLine("message name: {0}  message data: {1}", message.Name, message.Data);
        });

        Thread.Sleep(30000);

        ably.Connection.Close();

        Thread.Sleep(2000);

        Console.Out.WriteLine("Exiting...");
    }
}
