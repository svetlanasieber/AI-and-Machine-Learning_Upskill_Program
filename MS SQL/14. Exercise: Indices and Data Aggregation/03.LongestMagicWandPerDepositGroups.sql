SELECT
    [DepositGroup]
    , MAX([MagicWandSize]) as [LongestMagicWand]
FROM WizzardDeposits
GROUP BY DepositGroup
