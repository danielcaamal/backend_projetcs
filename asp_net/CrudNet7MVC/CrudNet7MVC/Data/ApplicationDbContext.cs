using Microsoft.EntityFrameworkCore;
using CrudNet7MVC.Models;

namespace CrudNet7MVC.Data
{
    public class ApplicationDbContext : DbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
            : base(options)
        {
        }
        

        public DbSet<Contact> Contacts { get; set; }
    }
}