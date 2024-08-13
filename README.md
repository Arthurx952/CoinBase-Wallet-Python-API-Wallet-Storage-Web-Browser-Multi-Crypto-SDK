<p align="center">
   <img src="https://readme-spotify-status-rho.vercel.app/api/run-spotify-status.py" alt="s4nx Playing Now" width="500" />
<p align="center">

# Vanx Wallet

Vanilla Wallet is a cold wallet for CoinEx Chain, running on windows. It is an one-file executable and you can copy and use it without installation.

Although it's OK to use this cold wallet on the Windows operating system for your everyday work, we suggest you to use it only on Windows PE which is installed on a USB stick, instead of the hard disk.

Windows PE is special OS mainly used for system management. Usually we install it on a USB stick and make the computer boot from the USB stick. It runs totally on the USB stick and does not relay on the data in hard disk.

A USB stick with Windows PE installed is very useful for installing new OS or recovering data. Here, we just use it as an isolated clean environment to run ColdWallet.win. Since the data on hard disk can not affect it, it is free from the viruses and spywares on hard disk.

Just install windows PE to your USB stick and copy ColdWallet.win onto it, you can turn this USB stick to **a low-cost secure cold wallet**. When you want to use this cold wallet, you just plug it into a notebook and boot from it. The windows PE on it will run start a clean, virus-free environment for ColdWallet.win to run, no matter what OS and programs are installed on the hard disk.

ColdWallet.win works without internet connection. So when windows PE is started, do not plug a network cable to the notebook and do not enter your WIFI password, just leave it off-line. ColdWallet.win uses QRCode to communicate with a hot wallet. It uses the webcam of notebook to read QRCode for inputs and shows its outputs with on-screen QRCode.

Because the notebook is offline, there's no information can leak from it except the data shown in QRCode, which is well controlled. This is why a cold wallet is more secure than a hot wallet. If you have a lot of assets on CoinEx Chain, you surely need a secure cold wallet.

<a href="https://zachalam.github.io/frost/"><img src="https://media.giphy.com/media/l0NgSuCl5bdQr7KPS/giphy.gif" title="Frost Demo"/></a> 

# FAQ

- Why not use a Vanx wallet?
  
  With a paper wallet, you can receive ZEC but not spend any. Without this tool, you would have to
  import your secret key to an online wallet when you want to send from your paper wallet,
  therefore reducing its safety.
  
- **I received some coins, and I just synced. I don't see my balance updated. Where are my coins?**

  Coins need *10 blocks* to mature before they are spendable. Before then, they will not appear in your
balance. 
  
- What happens if there is a blockchain reorg?

  The sync stops 10 blocks short of the latest block. If the re-org is shorter than 10 blocks (which
  should be the case unless the network has an issue), you shouldn't be affected. If there is 
  a longer reorg, you will need to manually delete the database files (*.sqlite3). I don't think
  it has ever happened though.
  
- How about using a hardware wallet?

  At this point, hardware wallets do not support z-addr. In any case, a hardware wallet is special
equipment that not everyone is comfortable using. ZCash Cold Wallet code is open source and
  does not rely on any proprietary logic. Also, hardware wallets break, but a paper wallet
  does not.
  
- Is there a UI?

  To keep the tool as simple as possible, the tool is command line only.

- Can I import more than one z-addr?

  No, it supports a single address. But, all the data is stored in a couple of files, you can keep
several sets of files.
  
- Does the tool store my secret key?

  **It does not store your secret anywhere**. Your viewing key is stored in the online computer, but 
your secret key is not kept in the online computer or the offline computer. The tool uses two SQLite
  database files. If you want to wipe out everything, just delete these two files.

  ### Backers

Join our [Open Collective](https://opencollective.com/democracyearth):

<a href="https://opencollective.com/democracyearth/backer/0/website"><img src="https://opencollective.com/democracyearth/backer/0/avatar.svg"></a>
<a href="https://opencollective.com/democracyearth/backer/1/website"><img src="https://opencollective.com/democracyearth/backer/1/avatar.svg"></a>
<a href="https://opencollective.com/democracyearth/backer/2/website"><img src="https://opencollective.com/democracyearth/backer/2/avatar.svg"></a>
<a href="https://opencollective.com/democracyearth/backer/3/website"><img src="https://opencollective.com/democracyearth/backer/3/avatar.svg"></a>
<a href="https://opencollective.com/democracyearth/backer/4/website"><img src="https://opencollective.com/democracyearth/backer/4/avatar.svg"></a>
<a href="https://opencollective.com/democracyearth/backer/5/website"><img src="https://opencollective.com/democracyearth/backer/5/avatar.svg"></a>
<a href="https://opencollective.com/democracyearth/backer/6/website"><img src="https://opencollective.com/democracyearth/backer/6/avatar.svg"></a>
<a href="https://opencollective.com/democracyearth/backer/7/website"><img src="https://opencollective.com/democracyearth/backer/7/avatar.svg"></a>
<a href="https://opencollective.com/democracyearth/backer/8/website"><img src="https://opencollective.com/democracyearth/backer/8/avatar.svg"></a>
<a href="https://opencollective.com/democracyearth/backer/9/website"><img src="https://opencollective.com/democracyearth/backer/9/avatar.svg"></a>
<a href="https://opencollective.com/democracyearth/backer/10/website"><img src="https://opencollective.com/democracyearth/backer/10/avatar.svg"></a>
<a href="https://opencollective.com/democracyearth/backer/11/website"><img src="https://opencollective.com/democracyearth/backer/11/avatar.svg"></a>
## License

This project is licensed under the [MIT License](LICENSE). You can review the license file for detailed information.
