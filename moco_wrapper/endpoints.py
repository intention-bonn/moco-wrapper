"""List of API Enpoints the moco wrapper knows about."""

API_PATH = {
    "employment_get":                   "/users/employments/{id}",
    "employment_getlist":               "/users/employments",
    "holiday_getlist":                  "/users/holidays",
    "holiday_get":                      "/users/holidays/{id}",
    "holiday_create":                   "/users/holidays",
    "holiday_update":                   "/users/holidays/{id}",
    "holiday_delete":                   "/users/holidays/{id}",
    "hourly_rate_get":                  "/account/hourly_rates",
    "invoice_getlist":                  "/invoices",
    "invoice_get":                      "/invoices/{id}",
    "invoice_locked":                   "/invoices/locked",
    "invoice_pdf":                      "/invoices/{id}.pdf",
    "invoice_timesheet":                "/invoices/{id}/timesheet.pdf",
    "invoice_update_status":            "/invoices/{id}/update_status",
    "invoice_create":                   "/invoices",
    "invoice_send_email":               "/invoices/{id}/send_email",
    "invoice_payment_getlist":          "/invoices/payments",
    "invoice_payment_get":              "/invoices/payments/{id}",
    "invoice_payment_create":           "/invoices/payments",
    "invoice_payment_update":           "/invoices/payments/{id}",
    "invoice_payment_delete":           "/invoices/payments/{id}",
    "invoice_payment_create_bulk":      "/invoices/payments/bulk",
    "offer_getlist":                    "/offers",
    "offer_get":                        "/offers/{id}",
    "offer_pdf":                        "/offers/{id}.pdf",
    "offer_create":                     "/offers",
    "offer_update_status":              "/offers/{id}/update_status",
    "presence_getlist":                 "/users/presences",
    "presence_get":                     "/users/presences/{id}",
    "presence_create":                  "/users/presences",
    "presence_update":                  "/users/presences/{id}",
    "presence_touch":                   "/users/presences/touch",
    "presence_delete":                  "/users/presences/{id}",
    "project_getlist":                  "/projects",
    "project_get":                      "/projects/{id}",
    "project_assigned":                 "/projects/assigned",
    "project_create":                   "/projects",
    "project_update":                   "/projects/{id}",
    "project_archive":                  "/projects/{id}/archive",
    "project_unarchive":                "/projects/{id}/unarchive",
    "project_report":                   "/projects/{id}/report",
    "project_contract_getlist":         "/projects/{project_id}/contracts",
    "project_contract_get":             "/projects/{project_id}/contracts/{contract_id}",
    "project_contract_create":          "/projects/{project_id}/contracts",
    "project_contract_update":          "/projects/{project_id}/contracts/{contract_id}",
    "project_contract_delete":          "/projects/{project_id}/contracts/{contract_id}",
    "project_expense_get":              "/projects/{project_id}/expenses/{expense_id}",
    "project_expense_getall":           "/projects/expenses",
    "project_expense_getlist":          "/projects/{project_id}/expenses",
    "project_expense_create":           "/projects/{project_id}/expenses",
    "project_expense_create_bulk":      "/projects/{project_id}/expenses/bulk",
    "project_expense_update":           "/projects/{project_id}/expenses/{expense_id}",
    "project_expense_delete":           "/projects/{project_id}/expenses/{expense_id}",
    "project_expense_disregard":        "/projects/{project_id}/expenses/disregard",
    "project_recurring_expense_getlist":"/projects/{project_id}/recurring_expenses",
    "project_recurring_expense_get":    "/projects/{project_id}/recurring_expenses/{recurring_expense_id}",
    "project_recurring_expense_create": "/projects/{project_id}/recurring_expenses",
    "project_recurring_expense_delete": "/projects/{project_id}/recurring_expenses/{recurring_expense_id}",
    "project_recurring_expense_update": "/projects/{project_id}/recurring_expenses/{recurring_expense_id}",
    "project_task_getlist":             "/projects/{project_id}/tasks",
    "project_task_get":                 "/projects/{project_id}/tasks/{task_id}",
    "project_task_create":              "/projects/{project_id}/tasks",
    "project_task_update":              "/projects/{project_id}/tasks/{task_id}",
    "project_task_delete":              "/projects/{project_id}/tasks/{task_id}",
    "unit_get":                         "/units/{id}",
    "unit_getlist":                     "/units",
    "schedule_get":                     "/schedules/{id}",
    "schedule_getlist":                 "/schedules",
    "schedule_create":                  "/schedules",
    "schedule_update":                  "/schedules/{id}",
    "schedule_delete":                  "/schedules/{id}",
    "project_payment_schedule_create":  "/projects/{project_id}/payment_schedules",
    "project_payment_schedule_getlist": "/projects/{project_id}/payment_schedules",
    "project_payment_schedule_get":     "/projects/{project_id}/payment_schedules/{schedule_id}",
    "project_payment_schedule_update":  "/projects/{project_id}/payment_schedules/{schedule_id}",
    "project_payment_schedule_delete":  "/projects/{project_id}/payment_schedules/{schedule_id}",
    "purchase_category_get":            "/purchases/categories/{id}",
    "purchase_category_getlist":        "/purchases/categories",
    "planning_entry_getlist":           "/planning_entries",
    "planning_entry_get":               "/planning_entries/{id}",
    "planning_entry_create":            "/planning_entries",
    "planning_entry_update":            "/planning_entries/{id}",
    "planning_entry_delete":            "/planning_entries/{id}",
    "tagging_add":                      "/taggings/{entity}/{entity_id}",
    "tagging_replace":                  "/taggings/{entity}/{entity_id}",
    "tagging_delete":                   "/taggings/{entity}/{entity_id}",
    "tagging_get":                      "/taggings/{entity}/{entity_id}",
}
