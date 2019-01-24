"""Plot time series data streamed through a dummy LSL outlet.
"""

import ble2lsl
from ble2lsl.devices import muse2016
from wizardhat import acquire, plot

device = muse2016
plot_stream = "EEG"

if __name__ == '__main__':
    dummy_outlet = ble2lsl.Dummy(device)
    receiver = acquire.Receiver()
    plot.Lines(receiver.buffers[plot_stream])