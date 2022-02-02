import HomeIcon from "@mui/icons-material/Home";
import EventIcon from "@mui/icons-material/Event";
import MonetizationOnIcon from "@mui/icons-material/MonetizationOn";
import CampaignIcon from "@mui/icons-material/Campaign";
import AssignmentIcon from "@mui/icons-material/Assignment";
import SettingsIcon from "@mui/icons-material/Settings";

import InventoryIcon from "@mui/icons-material/Inventory";

export const Links = [
  {
    title: "Dashboard",
    link: "/dashboard",
    icon: <HomeIcon />,
  },
  {
    title: "Credits",
    link: "/dashboard/credits",
    icon: <MonetizationOnIcon />,
  },
  {
    title: "Events",
    link: "/dashboard/events",
    icon: <EventIcon />,
  },
  {
    title: "Announcements",
    link: "/dashboard/announcements",
    icon: <CampaignIcon />,
  },
  {
    title: "Idea Bank",
    link: "/dashboard/idea-bank",
    icon: <InventoryIcon />,
  },
  {
    title: "Job Board",
    link: "/dashboard/job-board",
    icon: <AssignmentIcon />,
  },
  {
    title: "Settings",
    link: "/dashboard/settings",
    icon: <SettingsIcon />,
  },
];
