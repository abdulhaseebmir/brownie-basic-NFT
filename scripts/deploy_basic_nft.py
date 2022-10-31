from brownie import accounts, BasicNFT

def deploy_basic_nft():
    account = accounts[0]
    basic_nft = BasicNFT.deploy({"from": account})
    print(f"token counter: {basic_nft.getTokenCounter()}")
    tx = basic_nft.mintNFT()
    tx.wait(1)
    print(f"token counter: {basic_nft.getTokenCounter()}")


def main():
    deploy_basic_nft()