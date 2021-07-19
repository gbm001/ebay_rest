# coding: utf-8

# flake8: noqa

"""
    Marketing API

    <p>The <i>Marketing API </i> offers two platforms that sellers can use to promote and advertise their products:</p> <ul><li><b>Promoted Listings</b> is an eBay ad service that lets sellers set up <i>ad campaigns </i> for the products they want to promote. eBay displays the ads in search results and in other marketing modules as <b>SPONSORED</b> listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, see <a href=\"/api-docs/sell/static/marketing/promoted-listings.html\">Promoted Listings</a>.</li>  <li><b>Promotions Manager</b> gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \"20% off\" and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion <i>teasers</i> throughout buyer flows. For complete details, see <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a>.</li></ul>  <p><b>Marketing reports</b>, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.</p> <p class=\"tablenote\"><b>Important!</b> Sellers must have an active eBay Store subscription, and they must accept the <b>Terms and Conditions</b> before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \"requirements and restrictions\" sections for <a href=\"/api-docs/sell/marketing/static/overview.html#PL-requirements\">Promoted Listings</a> and <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager</a>.</p> <p>The table below lists all the Marketing API calls grouped by resource.</p>  # noqa: E501

    OpenAPI spec version: v1.10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from ..sell_marketing.api.ad_api import AdApi
from ..sell_marketing.api.ad_report_api import AdReportApi
from ..sell_marketing.api.ad_report_metadata_api import AdReportMetadataApi
from ..sell_marketing.api.ad_report_task_api import AdReportTaskApi
from ..sell_marketing.api.campaign_api import CampaignApi
from ..sell_marketing.api.item_price_markdown_api import ItemPriceMarkdownApi
from ..sell_marketing.api.item_promotion_api import ItemPromotionApi
from ..sell_marketing.api.promotion_api import PromotionApi
from ..sell_marketing.api.promotion_report_api import PromotionReportApi
from ..sell_marketing.api.promotion_summary_report_api import PromotionSummaryReportApi
# import ApiClient
from ..sell_marketing.api_client import ApiClient
from ..sell_marketing.configuration import Configuration
# import models into sdk package
from ..sell_marketing.models.ad import Ad
from ..sell_marketing.models.ad_ids import AdIds
from ..sell_marketing.models.ad_paged_collection import AdPagedCollection
from ..sell_marketing.models.ad_reference import AdReference
from ..sell_marketing.models.ad_references import AdReferences
from ..sell_marketing.models.ad_response import AdResponse
from ..sell_marketing.models.ads import Ads
from ..sell_marketing.models.amount import Amount
from ..sell_marketing.models.base_response import BaseResponse
from ..sell_marketing.models.bulk_ad_response import BulkAdResponse
from ..sell_marketing.models.bulk_create_ad_request import BulkCreateAdRequest
from ..sell_marketing.models.bulk_create_ads_by_inventory_reference_request import BulkCreateAdsByInventoryReferenceRequest
from ..sell_marketing.models.bulk_create_ads_by_inventory_reference_response import BulkCreateAdsByInventoryReferenceResponse
from ..sell_marketing.models.bulk_delete_ad_request import BulkDeleteAdRequest
from ..sell_marketing.models.bulk_delete_ad_response import BulkDeleteAdResponse
from ..sell_marketing.models.bulk_delete_ads_by_inventory_reference_request import BulkDeleteAdsByInventoryReferenceRequest
from ..sell_marketing.models.bulk_delete_ads_by_inventory_reference_response import BulkDeleteAdsByInventoryReferenceResponse
from ..sell_marketing.models.campaign import Campaign
from ..sell_marketing.models.campaign_criterion import CampaignCriterion
from ..sell_marketing.models.campaign_paged_collection import CampaignPagedCollection
from ..sell_marketing.models.campaigns import Campaigns
from ..sell_marketing.models.clone_campaign_request import CloneCampaignRequest
from ..sell_marketing.models.coupon_configuration import CouponConfiguration
from ..sell_marketing.models.create_ad_request import CreateAdRequest
from ..sell_marketing.models.create_ads_by_inventory_reference_request import CreateAdsByInventoryReferenceRequest
from ..sell_marketing.models.create_ads_by_inventory_reference_response import CreateAdsByInventoryReferenceResponse
from ..sell_marketing.models.create_campaign_request import CreateCampaignRequest
from ..sell_marketing.models.create_report_task import CreateReportTask
from ..sell_marketing.models.delete_ad_request import DeleteAdRequest
from ..sell_marketing.models.delete_ad_response import DeleteAdResponse
from ..sell_marketing.models.delete_ads_by_inventory_reference_request import DeleteAdsByInventoryReferenceRequest
from ..sell_marketing.models.delete_ads_by_inventory_reference_response import DeleteAdsByInventoryReferenceResponse
from ..sell_marketing.models.dimension import Dimension
from ..sell_marketing.models.dimension_key_annotation import DimensionKeyAnnotation
from ..sell_marketing.models.dimension_metadata import DimensionMetadata
from ..sell_marketing.models.discount_benefit import DiscountBenefit
from ..sell_marketing.models.discount_rule import DiscountRule
from ..sell_marketing.models.discount_specification import DiscountSpecification
from ..sell_marketing.models.error import Error
from ..sell_marketing.models.error_parameter import ErrorParameter
from ..sell_marketing.models.funding_strategy import FundingStrategy
from ..sell_marketing.models.inventory_criterion import InventoryCriterion
from ..sell_marketing.models.inventory_item import InventoryItem
from ..sell_marketing.models.inventory_reference import InventoryReference
from ..sell_marketing.models.item_price_markdown import ItemPriceMarkdown
from ..sell_marketing.models.item_promotion import ItemPromotion
from ..sell_marketing.models.item_promotion_response import ItemPromotionResponse
from ..sell_marketing.models.metric_metadata import MetricMetadata
from ..sell_marketing.models.promotion_detail import PromotionDetail
from ..sell_marketing.models.promotion_report_detail import PromotionReportDetail
from ..sell_marketing.models.promotions_paged_collection import PromotionsPagedCollection
from ..sell_marketing.models.promotions_report_paged_collection import PromotionsReportPagedCollection
from ..sell_marketing.models.report_metadata import ReportMetadata
from ..sell_marketing.models.report_metadatas import ReportMetadatas
from ..sell_marketing.models.report_task import ReportTask
from ..sell_marketing.models.report_task_paged_collection import ReportTaskPagedCollection
from ..sell_marketing.models.rule_criteria import RuleCriteria
from ..sell_marketing.models.selected_inventory_discount import SelectedInventoryDiscount
from ..sell_marketing.models.selection_rule import SelectionRule
from ..sell_marketing.models.summary_report_response import SummaryReportResponse
from ..sell_marketing.models.update_bid_percentage_request import UpdateBidPercentageRequest
from ..sell_marketing.models.update_campaign_identification_request import UpdateCampaignIdentificationRequest
