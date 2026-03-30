# Custom Optimization Algorithms

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/CustomOptimizationAlgorithms
- Category: Guides

---

# Custom Optimization Algorithms

The Trade Desk offers the following custom optimization algorithms:

| Algorithm | Description |
| [Dimensional Bidding](/v3/portal/api/doc/BYOADimensionalBidding) | As a feature, [dimensional bidding](/v3/portal/api/doc/DimensionalBidding) allows you to apply one bid factor to a combination of target vector values. For example, you could apply a bid factor of 3.14 to the combination of mobile (device type) and Singapore (geo). If you targeted each of those vectors separately with a different bid factor, your two bid factors would multiply together. Multiplying multiple bid factors together to target precise, high-value market niches can result in unnecessarily high bids, which may result in the need for a max bid to act as a cap on your bid possibilities. To solve for this, you can extend your current ad group strategy with dimensional bidding to look for small pockets of high value while avoiding an exponential rise in bid value. |
| [User Scoring](/v3/portal/api/doc/UserScoringBaseBidCPM) | By default, ad groups assign all users in an audience the same base bid for each impression. User scoring provides an opportunity to assign a discrete bid value for each user, thus allowing a partner to override an ad group's base bid when creating data segments in The Trade Desk platform. This functionality combined with the data available in [REDS](/v3/portal/reds/doc/REDSGeneralInfo) solves the problem of determining the value of users that haven't been seen before. |