package com.example.socialsafety;

import androidx.appcompat.app.AppCompatActivity;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
    BluetoothAdapter mBluetoothAdapter;
    public ArrayList<BluetoothDevice> list;
    StringBuilder sbName = new StringBuilder();
    StringBuilder sbAdd = new StringBuilder();

    private final BroadcastReceiver receiver = new BroadcastReceiver() {
        public void onReceive(Context context, Intent intent) {
            String action = intent.getAction();
            if (BluetoothDevice.ACTION_FOUND.equals(action)) {
                // Discovery has found a device. Get the BluetoothDevice
                // object and its info from the Intent.
                BluetoothDevice device = intent.getParcelableExtra(BluetoothDevice.EXTRA_DEVICE);
                String deviceName = device.getName();
                String deviceHardwareAddress = device.getAddress(); // MAC address
                Log.d("XXX", deviceName);
            }
        }
    };
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button toggleBtn = (Button) findViewById(R.id.buttonToggle);
        Button scan = (Button) findViewById((R.id.scan));
        mBluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
        list = new ArrayList<BluetoothDevice>();

        scan.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.d("x","Pressed");
                if(mBluetoothAdapter.disable())
                    enableDisableBT();
                if(mBluetoothAdapter.isDiscovering()){
                    mBluetoothAdapter.cancelDiscovery();
                    mBluetoothAdapter.startDiscovery();
                    IntentFilter scanner = new IntentFilter(BluetoothDevice.ACTION_FOUND);
                    registerReceiver(receiver, scanner);
                    Log.d("s", "isDiscovenig");
                }
                if(!mBluetoothAdapter.isDiscovering()){
                    IntentFilter scanner = new IntentFilter(BluetoothDevice.ACTION_FOUND);
                    registerReceiver(receiver, scanner);
                    Log.d("Tr", "Trying to on");
                }
            }
        });

        toggleBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                enableDisableBT();
                Log.d("Z","BT ON");
            }
        });

    }
    public void enableDisableBT(){
        if(mBluetoothAdapter == null){
            Log.d("Not working", "BT not supported");
        }
        if(!mBluetoothAdapter.isEnabled()) {
            Intent enable = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
//            enable.putExtra(BluetoothAdapter.EXTRA_DISCOVERABLE_DURATION, 3600);
            startActivity(enable);
        }
        if(mBluetoothAdapter.isEnabled()){
            mBluetoothAdapter.disable();
        }
    }

}
