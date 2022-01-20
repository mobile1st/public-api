from __future__ import absolute_import, division, print_function
from core import models as m

modelsmap = {
    m.AxieNftEvent: [
        "id",
        "nft_id",
        "price",
        "price_usd",
        "seller_id",
        "buyer_id",
        "created_date",
        "event_date",
        "block_chain_id",
        "seller",
        "buyer"
    ],
    m.AxieNft: [
        "id",
        "axie_id",
        "name",
        "avatar",
        "axie_class",
        "genes",
        "body_shape",
        "sire_id",
        "sire_class",
        "matron_id",
        "matron_class",
        "stage",
        "title",
        "breed_count",
        "level",
        "created_date",
        "parts",
        "childs"
    ],
    m.AxieUser: [
        "id",
        "account_id",
        "name",
        "ronin_address",
        "eth_address",
        "loom_address",
        "tomo_address"
    ]
}
